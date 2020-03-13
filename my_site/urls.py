from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url

app_name = 'my_site'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mysite/index.html'), name='index'),
]