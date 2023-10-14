from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

class User(AbstractBaseUser):
    NULLABLE = {'blank': True, 'null': True}

    username = None

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
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()
