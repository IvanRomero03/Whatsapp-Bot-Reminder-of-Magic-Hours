import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = ""

datetime = time.localtime()

hora = datetime.tm_hour
minuto = datetime.tm_min

mensaje = str(hora % 12) + ":" + str(minuto)

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    to='whatsapp:+',
    body=mensaje
)

print(message.sid)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    to='whatsapp:+',
    body=mensaje
)

print(message.sid)
