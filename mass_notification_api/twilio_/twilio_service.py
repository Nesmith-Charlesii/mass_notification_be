from django.conf import settings
from twilio.rest import Client

def send_sms(phone_number, message_body):
  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

  message = client.messages.create(
    from_= settings.TWILIO_NUMBER,
    to= phone_number,
    body= message_body
  )

  print(message.sid)