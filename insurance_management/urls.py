from django.urls import path
from insurance_management.views import InsuranceCreateView, InsuranceUpdateView, InsuranceDeleteView

urlpatterns = [
    path('insurance/add/', InsuranceCreateView.as_view(), name='insurance_add'),
    path('insurance/<str:insurance_code>/edit/', InsuranceUpdateView.as_view(), name='insurance_edit'),
    path('insurance/<str:insurance_code>/delete/', InsuranceDeleteView.as_view(), name='insurance_delete'),
]
