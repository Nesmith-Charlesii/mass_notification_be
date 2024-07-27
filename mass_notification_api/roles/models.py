from django.db import models
from users.models import CustomUser

class Role(models.Model):
    role = models.CharField(max_length=30, unique=True)
    users = models.ManyToManyField(CustomUser, related_name='roles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Role: {self.role}\nUser: {self.user}'