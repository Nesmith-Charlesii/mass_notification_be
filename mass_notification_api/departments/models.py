from django.db import models
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    head_of_department = models.ForeignKey(CustomUser, related_name="departments", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(CustomUser, related_name="departments", on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.name}\nDepartment head: {self.head_of_department}\n{self.phone_number}\nLast modified: {self.last_modified}'