from django.db import models


# Create your models here.
class Patient(models.Model):
    fist_name = models.CharField(max_length=64, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=64, verbose_name='Фамилия', null=True, blank=True)
    # email = models.EmailField(max_length=128, verbose_name='Электронная почта', null=True, blank=True)
    phone_number = models.CharField(max_length=64, verbose_name='Номер телефона', null=True, blank=True)
    # comment = models.TextField('Комментарий', null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Время обращения')
    # status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.fist_name} {self.last_name} {self.phone_number}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


