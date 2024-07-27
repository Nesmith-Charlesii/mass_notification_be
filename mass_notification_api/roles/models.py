from django.db import models
from users.models import CustomUser

class Role(models.Model):
    role = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField(CustomUser, related_name='roles', blank=True)
    def __repr__(self):
        return f'Role: {self.role}\nUser: {self.user}' 