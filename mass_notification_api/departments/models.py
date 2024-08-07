from django.db import models
from users.models import CustomUser

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    head_of_department = models.ForeignKey(CustomUser, related_name="is_department_head", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(CustomUser, related_name="departments", blank=True)

    def __repr__(self):
        return f'{self.name}\nDepartment head: {self.head_of_department}\n{self.phone_number}\nLast modified: {self.last_modified}'