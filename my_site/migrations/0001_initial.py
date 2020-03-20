# Generated by Django 3.0.4 on 2020-03-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=128, null=True, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(blank=True, max_length=64, null=True, verbose_name='Номер телефона')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время обращения')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
    ]
