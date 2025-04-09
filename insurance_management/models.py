from django.db import models
from authentication.models import Client

class Insurance(models.Model):
    insurance_code = models.CharField(max_length=8, primary_key=True, editable=False)
    TYPE={
        ('health', 'health'),
        ('life', 'life'),
        ('auto', 'auto'),
        ('home', 'home'),

    }
    insurance_type = models.CharField(max_length=100, choices=TYPE)

    

class Client_Insurance(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)  
    suscription_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()