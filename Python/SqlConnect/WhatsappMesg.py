from twilio.rest import Client

account_sid = 'XXXX'
auth_token = 'XXXX'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello there!',
    from_='whatsapp:+12162385553',
    to='whatsapp:+917815016866')

print(message.sid)