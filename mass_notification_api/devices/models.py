from django.db import models
from users.models import CustomUser

class Device(models.Model):
    # An immutable list of device choices implemented at the model level to prevent invalid data from being stored in the DB in the case of frontend form comprimises.
    DEVICE_CHOICES = [
        ('phone', 'Phone'),
        ('laptop', 'Laptop')
    ]

    device_type = models.CharField(
        max_length=10,
        choices=DEVICE_CHOICES,
        default='phone'
    )
    brand_name = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(CustomUser, related_name='devices', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)