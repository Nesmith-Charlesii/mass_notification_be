from twilio.rest import Client

account_sid = 'ACd40bf12b3efbc9aec638e752315817c5'
auth_token = '6ea1346a764e27882f7480c6cd81e56a'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_= '+18335320199',
  to= '+19198021911'
)

print(message.sid)