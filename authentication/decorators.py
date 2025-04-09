from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse 

from authentication.models import Client

def guest_only(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if isinstance(user, Client):
                return redirect(reverse('client_profil:client_home_profil',kwargs={'entreprise':user.pk}))   
        return view_func(request, *args, **kwargs)   
    return wrapper