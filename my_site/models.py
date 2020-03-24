from django.db import models


# Create your models here.
class Patient(models.Model):
    fist_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=64, verbose_name='Номер телефона')
    comment = models.TextField('Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время обращения')
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.fist_name} {self.last_name} {self.phone_number}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


