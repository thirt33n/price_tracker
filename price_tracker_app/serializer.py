from rest_framework import serializers
from .models import Alerts

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields=['id','user','price_targ','status']
        