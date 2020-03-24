from django.urls import path

from . import views

from .views import set_webhook, ViberUserView

app_name = 'viber_bot'

urlpatterns = [
    path('callback/', views.callback),
    path('set_webhook/', set_webhook),
    path('hi/', ViberUserView.as_view()),
]
