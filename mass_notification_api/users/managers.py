from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        if not password: 
            raise ValueError(_("The Password must be set"))
        email = self.normalize_email(email)

        """
        password=password is not directly set when instantiating a user object. That is what 'user.set_password' is for.
        'user.set_password securely hashes and sets a password.
        adding 'password=password to self.model would store the password in plain text, which is a security risk.
        """

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password
        """

        # The 'setdefault' method checks if the field exists during instantiation. If not, it creates the field and assigns it a default value. Arg 1 is the key, Arg 2 is the value.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(email, password, **extra_fields)