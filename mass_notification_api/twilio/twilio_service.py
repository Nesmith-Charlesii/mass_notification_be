from django.conf import settings
from twilio.rest import Client

def send_sms(user):
  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

  message = client.messages.create(
    from_= '+18335320199',
    to= settings.TWILIO_TO_NUMBER
  )

  print(message.sid)