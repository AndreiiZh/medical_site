from django.urls import path, include

from . import views
# from .views import set_webhook
from .views import set_webhook, ViberUserView

urlpatterns = [
    path('callback/', views.callback),
    path('set_webhook/', set_webhook),
    path('hi/', ViberUserView.as_view()),
]