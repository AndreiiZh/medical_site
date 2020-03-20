from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'my_site'

urlpatterns = [
    path('', views.PatientView.as_view(template_name='mysite/index.html'), name='home'),

]
