from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from authentication.services import userServices
from authentication.repositories import userRepositories
from django.contrib import messages

def home(request):
    return render(request, 'authentication/home.html')


def add_employee_view(request):
    if request.method == "POST":
        service = userServices(userRepositories())
        try:
            service.create_new_client(request.POST)
            messages.success(request, "Employé ajouté avec succès.")
            return redirect("employee_list")
        except Exception as e:
            messages.error(request, f"Erreur : {str(e)}")
    
    return render(request, "create_employee.html")
