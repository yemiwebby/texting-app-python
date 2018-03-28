from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)


my_msg = ''.join(['Sample integration \n' for i in range(50)])

# my_msg = "Just trying out this awesome messaging app powered by Twilio using Python."

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)

# call = client.calls.create(to=my_cell, from_=my_twilio, url=my_url)