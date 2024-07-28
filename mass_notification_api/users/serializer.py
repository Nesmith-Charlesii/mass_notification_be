from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "title",
            "email",
            "phone_number",
            "date_joined",
            "is_active",
            "is_staff"
        ]