from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Alerts
from .serializer import AlertSerializer
from .export_binance import getPrice


from rest_framework.response import Response
import requests

class AlertViews(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer

    @action(detail=True, methods=['post'])
    def alert_trigger(self,request,pk=None):
        alerter = self.get_object()
        
        #Use requests to get current price here
        
        cur_price_default = getPrice()
        
        #cur_price_default = 38000 #Placeholder for testing
       
        if alerter.price_targ > cur_price_default :
            alerter.status = 'triggered'
            alerter.save()
            print("Price dropped below target cur_price: ",cur_price_default)
            
            
            
            #requests.post("https://ntfy.sh/oxost",      #Testing before email implementation using ntfy for notifications
            #data="Price Dropped".encode(encoding='utf-8'))
            
            
            return Response({'status': 'Alert Triggered'})
        else:
            print("Price :",cur_price_default)
            return Response({'status':'Price not dropped'})
        



    def create(self,request, *args, **kwargs):
        allowed_fields = {'user', 'price_targ'}
        data = {key: request.data[key] for key in allowed_fields if key in request.data}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        data['status']  = 'created'
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'Alert Created'})
            
