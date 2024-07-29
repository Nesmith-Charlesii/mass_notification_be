from rest_framework import serializers
from models import Device

class DeviceSerializer(serializers.Serializer):
    class Meta:
        model = Device
        fields = "__all__"