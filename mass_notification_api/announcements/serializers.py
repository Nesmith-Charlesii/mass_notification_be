from rest_framework import serializers
from models import Announcement

class AnnouncementSerializer(serializers.Serializer):
    class Meta:
        model = Announcement
        fields = '__all__'