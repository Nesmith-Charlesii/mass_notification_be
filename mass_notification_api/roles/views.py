from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from models import Role
from serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer