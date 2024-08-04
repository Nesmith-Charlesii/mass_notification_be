from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    # The 'validated_data' param is a built-in function of DRF
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name = validated_data.get("first_name", ""),
            last_name = validated_data.get("last_name", ""),
            email = validated_data["email"],
            phone_number = validated_data.get("phone_number", ""),
            password = validated_data["password"]
        )
        return user