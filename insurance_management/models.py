from django.db import models
from authentication.models import Client,Manager

class Insurance(models.Model):
    TYPE={
        ('health', 'health'),
        ('life', 'life'),
        ('auto', 'auto'),
        ('home', 'home'),
    }
    insurance_code = models.CharField(max_length=8, primary_key=True, editable=False)
    client = models.ForeignKey(Client, related_name='+', on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager,related_name='+', on_delete=models.CASCADE)
    insurance_type = models.CharField(max_length=100, choices=TYPE)
    suscription_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
 