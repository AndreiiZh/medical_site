from urllib import request

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views import generic
from django.core.mail import send_mail

from .form import PatientForm
from .models import Patient


# Create your views here.
class PatientView(FormView):
    model = Patient
    form_class = PatientForm
    template_name = 'mysite/index.html'
    success_message = 'Success'
    success_url = reverse_lazy('my_site:home')

    def form_valid(self, form):
        fist_name = form.cleaned_data['fist_name']
        last_name = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        message = ('Данные пациента:\nИмя и Фамилия - ' + str(fist_name) + ' ' + str(last_name) + '\nНомер телефона - ' + str(phone_number) + '\nЭлектронная почта - ' + str(email) + '\nКомментарий:\n' + str(comment))
        send_mail('Запись', message, 'kireeva@neurologzp.com.ua', ['zhylin88888@gmail.com'])
        form.save()
        return super().form_valid(form)
