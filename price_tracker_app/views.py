from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Alerts
from .serializer import AlertSerializer
from .export_binance import getPrice
from rest_framework.response import Response
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command
from .tasks import send_email_task

class AlertViews(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer

    def alert_trigger(self):
        cur_price_default = getPrice()
        
        triggered_alerts = Alerts.objects.filter(price_targ__gt=cur_price_default, status='created')

        for alert in triggered_alerts:
            alert.status = 'triggered'
            alert.save()
            print(f"Price Dropped below for id: {alert.id} Current Price:  {cur_price_default}")

            send_email_task.delay(
                subject='BTC PRICE DROPPED BELOW YOUR TARGET',
                message=f'THE BTC PRICE HAS DROPPED BELOW YOUR SET TARGET OF {alert.price_targ} the current BTC price is: {cur_price_default}.',
                from_email='trial@example.com',
                recipient_list=[alert.email],
            )

        



    def create(self,request, *args, **kwargs):
        allowed_fields = {'user', 'price_targ','email'}
        data = {key: request.data[key] for key in allowed_fields if key in request.data}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        data['status']  = 'created'
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'Alert Created'})


    @action(detail=False, methods=['get'])
    def check(self, request):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.alert_trigger, 'interval', minutes=2)
        scheduler.start()
        return Response({'status': 'Periodic check started'})
        
            
