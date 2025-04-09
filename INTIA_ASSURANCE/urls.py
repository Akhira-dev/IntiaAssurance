
from django.contrib import admin
from django.urls import path,include
from authentication.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('insurance/', include('insurance_management.urls')),

]
