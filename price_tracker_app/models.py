from django.db import models
from django.contrib.auth.models import User


class Alerts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    price_targ=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20, default='created')
    email=models.EmailField(default='abc@example.com') 