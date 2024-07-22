from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    #department field needed
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager() # 'objects' is used to define a manager for a model. These creates an instance of custom user manager class to perform queries.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']