from rest_framework import serializers
from models import Role

class RoleSerializer(serializers.Serializer):
    class Meta:
        model = Role
        fields = '__all__'