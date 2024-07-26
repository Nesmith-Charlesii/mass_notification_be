from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # PermissionsMixin automatically includes 'is_superuser' to the CustomUser model. 'is_superuser = models.BooleanField(default=False)' is not neccessary.
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # 'objects' is used to define a manager for a model. These creates an instance of custom user manager class to perform queries.
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    ## REQUIRED_FIELDS is only related to superuser creation. Django will prompt for these fields in addition to the USERNAME_FIELD
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __repr__(self):
        return f'{self.first_name} {self.last_name}\n{self.title}\n{self.email}\n{self.phone_number}\nDate joined: {self.date_joined}\n{self.is_active}'