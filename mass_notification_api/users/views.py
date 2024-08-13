from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ..twilio import twilio_service

class UserViewSet(viewsets.ModelViewSet): 
    '''
    The queryset defines the data that the viewset will work with. In this case, all user objects are available to the viewsets module
    The viewset will use this queryset to perform various CRUD operations.
    '''
    queryset = CustomUser.objects.all()

    '''This tells the viewset which serializer to use when converting CustomUser instances to JSON (or other formats) and vice versa'''
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['post'], url_path='nofify_user')
    def notify_user(self, request, pk=None):
        user = self.get_object()
        phone_number = user.phone_number
        message_body = f'Yo what\'s good {user.first_name}!'

        twilio_service.send_sms(phone_number, message_body)

        return Response({'status': 'SMS sent'}, status=status.HTTP)