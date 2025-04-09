from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Insurance
from .forms import InsuranceForm
from insurance_management.services import insuranceServices  

class InsuranceCreateView(CreateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = 'insurance/insurance_form.html'
    success_url = reverse_lazy('insurance_list')   

    def form_valid(self, form):
        insurance = form.save(commit=False)
        insurance.insurance_code = insuranceServices.generate_insurance_code()
        insurance.save()
        return super().form_valid(form)

class InsuranceUpdateView(UpdateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = 'insurance/insurance_form.html'
    success_url = reverse_lazy('insurance_list')  
    pk_url_kwarg = 'insurance_code'
    slug_field = 'insurance_code'
    slug_url_kwarg = 'insurance_code'


class InsuranceDeleteView(DeleteView):
    model = Insurance
    template_name = 'insurance/insurance_confirm_delete.html'
    success_url = reverse_lazy('insurance_list')   
    pk_url_kwarg = 'insurance_code'
    slug_field = 'insurance_code'
    slug_url_kwarg = 'insurance_code'
