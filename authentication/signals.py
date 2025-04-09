from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,post_delete,pre_delete

from authentication.models import Client
from authentication.services import userServices,userEmailService
from utils import get_request
        
@receiver(pre_save, sender=Client)
def set_employee_code_using_trigger(sender, instance, **kwargs):
    code = userServices.generate_unique_employee_code() 
    if not instance.code:
        instance.code = code


@receiver(post_save, sender=Client)
def sent_email_user_after_create(sender, instance, created, **kwargs):
    if created:
        email_service = userEmailService()
        request = get_request()
        try:
            email_service.send_mail_to_user(request,instance)
        except Exception as e:
            raise ValueError(str(e))