from django.db import models


# Create your models here.
class ViberUser(models.Model):
    name = models.CharField(max_length=56, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    viber_id = models.CharField(max_length=36, null=True, blank=True)
    language = models.CharField(max_length=8, null=True, blank=True)
    country = models.CharField(max_length=8, null=True, blank=True)
    primary_device_os = models.CharField(max_length=56, null=True, blank=True)
    device_type = models.CharField(max_length=56, null=True, blank=True)
    api_version = models.CharField(max_length=56, null=True, blank=True)
    viber_version = models.CharField(max_length=56, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
