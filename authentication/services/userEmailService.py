from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from authentication.token import account_activate_token

class EmailService:
 
    def send_mail_to_user(self,request,user):

        message_data = {
            'domain':get_current_site(request).domain,
            'protocol':'https' if request.is_secure() else 'http',
            'user':user if user else None,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activate_token.make_token(user),
        }
        
        template_mail = "Authentication/template_mail.html"
        mail_subject = "Information compte employé"
        to_email = [user.email]
        message = render_to_string(template_mail,message_data)
        email = EmailMessage(mail_subject, message, to=to_email)
        email.content_subtype = 'html'
        email.send() 
