from django.urls import path
from authentication.views import *

urlpatterns = [
    path('intia/', home, name='insurance'),
    # path('add-user/', InsuranceCreateView.as_view(), name='insurance_add'),
     
]
