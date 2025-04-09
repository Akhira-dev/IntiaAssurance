from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,post_delete,pre_delete

from insurance_management.models import Insurance
from insurance_management.services import insuranceServices
from utils import get_request
        
@receiver(pre_save, sender=Insurance)
def generate_insurance_code(sender, instance, **kwargs):
    code = insuranceServices.generate_insurance_code() 
    if not instance.code:
        instance.code = code