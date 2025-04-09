
from django.contrib.auth.hashers import make_password

from authentication.exceptions import ClientNotFoundError
from authentication.models import Client
  
class ClientRepository:

    def add_client(self,client_datas):
        password = client_datas.pop('password')
        client = Client(**client_datas)
        client.password = make_password(password)
        client.save()
        return client
     
    def list_of_client(self):
        return Client.objects.all()
    
    def get_client_with_code(self,client_code):
        try:
            return Client.objects.filter(code=client_code).first()
        except Client.DoesNotExist:
            return  None
       

    def update_client_using_code(self,client_code):
        pass 
    
    def delete_client_by_code(self,client_code):
        try:
            client = Client.objects.get(code=client_code)
            client.delete()
            return True
        except Client.DoesNotExist:
            raise ClientNotFoundError(f"L'employé avec le code {client_code} n'existe pas.")



    
