from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views import generic

from bootstrap_modal_forms.generic import BSModalCreateView

from .form import PatientForm
from .models import Patient


# Create your views here.
class PatientView(FormView):
    model = Patient
    form_class = PatientForm
    template_name = 'mysite/index.html'
    success_message = 'Success'
    success_url = reverse_lazy('my_site:home')

    # success_url = 'http://127.0.0.1:8000'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



