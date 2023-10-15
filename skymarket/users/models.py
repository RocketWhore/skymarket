from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    NULLABLE = {'blank': True, 'null': True}
    username = models.CharField(max_length=35, **NULLABLE)
    first_name = models.CharField(max_length=35, verbose_name='имя')
    last_name = models.CharField(max_length=35, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = PhoneNumberField(unique=True)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('admin', 'Admin')])
    image = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    # - first_name — имя пользователя (строка).
    # - last_name — фамилия пользователя (строка).
    # - phone — телефон для связи (строка).
    # - email — электронная почта пользователя (email) **(используется в качестве логина).**
    # - role — роль пользователя, доступные значения: user, admin.
    # - image - аватарка пользователя

    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role", 'username']

