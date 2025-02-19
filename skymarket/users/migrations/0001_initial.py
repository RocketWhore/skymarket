# Generated by Django 3.2.6 on 2023-10-11 14:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=35, verbose_name='имя')),
                ('last_name', models.CharField(max_length=35, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='аватар')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
