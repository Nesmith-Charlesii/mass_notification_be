from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from twilio.twilio_service import send_sms

class UserViewSet(viewsets.ModelViewSet): 
    '''
    The queryset defines the data that the viewset will work with. In this case, all user objects are available to the viewsets module
    The viewset will use this queryset to perform various CRUD operations.
    '''
    queryset = CustomUser.objects.all()

    '''This tells the viewset which serializer to use when converting CustomUser instances to JSON (or other formats) and vice versa'''
    serializer_class = CustomUserSerializer

    '''
    By using 'detail=True', DRF knows to include an ID in the URL when using viewsets.
    It tells DRF to operate on a single instance
    '''
    @action(detail=True, methods=['get', 'post'], url_path='notify_user')
    def notify_user(self, request, pk=None):
        # Automatically retrieves object ID passed in URL and passes it to this method
        user = self.get_object()
        phone_number = user.phone_number
        message_body = f'Yo what\'s good {user.first_name}!'

        send_sms(phone_number, message_body)

        return Response({'status': 'SMS sent'}, status=status.HTTP_200_OK)