import random,string

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from authentication.repositories import userRepositories
from authentication.models import Client
from authentication.forms import ClientForm
from authentication.exceptions import ClientNotFoundError

class EmployeeUserService:

    def __init__(self, user_repository:userRepositories):
        self.user_repository = user_repository

    @staticmethod
    def generate_unique_client_code():
        while True:
            random_number = ''.join(random.choices(string.digits,k=5))
            client_code = f'ETG{random_number}'
            if not Client.objects.filter(code=random_number).exists():
                return client_code
    
    def create_new_client(self, client_data):
        form = ClientForm(client_data)
        if form.is_valid():
            validated_data = form.cleaned_data
            validated_data.pop('confirm_password', None)
            return self.user_repository.add_client(validated_data)
        else:
            raise ValidationError(form.errors)
    
   
    def get_list_of_client(self):
        return self.user_repository.list_of_client()
    
  
    def get_client_by_code(self,client_code):
        return self.user_repository.get_client_with_code(client_code)
    
    def delete_client(self,client_code):
        try:
            return self.user_repository.delete_employe_by_code(client_code)
        except ClientNotFoundError as e:
            return False
    

