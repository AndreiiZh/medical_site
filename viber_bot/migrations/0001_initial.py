# Generated by Django 3.0.4 on 2020-03-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViberUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=56, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('viber_id', models.CharField(blank=True, max_length=36, null=True)),
                ('language', models.CharField(blank=True, max_length=8, null=True)),
                ('country', models.CharField(blank=True, max_length=8, null=True)),
                ('primary_device_os', models.CharField(blank=True, max_length=56, null=True)),
                ('device_type', models.CharField(blank=True, max_length=56, null=True)),
                ('api_version', models.CharField(blank=True, max_length=56, null=True)),
                ('viber_version', models.CharField(blank=True, max_length=56, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
