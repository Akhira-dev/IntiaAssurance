from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.manager import CustomUserManager

class User(AbstractBaseUser,PermissionsMixin):
    code = models.CharField(max_length=8, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Professional E-mail")
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_supended = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name
     
 
class Client(User):
    
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10,)
    nationality  = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Manager(User):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"