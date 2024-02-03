from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Alerts
from .serializer import AlertSerializer
from rest_framework.response import Response


class AlertViews(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer

    @action(detail=True, methods=['post'])
    def alert_trigger(self,request,pk=None):
        alerter = self.get_object()
        cur_price_default = 38000
        if(alerter.price_targ > cur_price_default):
            alerter.status = 'triggered'
            alerter.save()
            print("Price dropped below target")
            return Response({'status: Alert Triggered'})



    def create(self,request, *args, **kwargs):
        allowed_fields = {'user', 'price_targ'}
        data = {key: request.data[key] for key in allowed_fields if key in request.data}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        data['status']  = 'created'
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'Done'})
            


# Create your views here.
