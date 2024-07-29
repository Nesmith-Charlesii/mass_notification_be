from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from serializers import AnnouncementSerializer
from models import Announcement

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer