# /usr/bin/env python
from twilio.rest import Client
import config as cfg

global numbers, account_sid, auth_token

twilioNumber = cfg.configuration['twilioNumber']
station = cfg.configuration['stationNumber']

# Find these values at https://twilio.com/user/account
account_sid = cfg.configuration['account_sid']
auth_token = cfg.configuration['twilio_auth_Token']

client = Client(account_sid, auth_token)

def send(text,number):
    context = "Context: %s Call this number to win %s" % (text, station)
    client.api.account.messages.create(
    to=number,
    from_=twilioNumber,
    body=context)
    client.api.account.messages.create(
    to="+16197182387",
    from_=twilioNumber,
    body=context)

def test():
    text = 'This is a test'
    context = "Context: %s Call this number to win %s" % (text, station)
    for number in numbers:
        client.api.account.messages.create(
        to=number,
        from_=twilioNumber,
        body=context)


if __name__ == '__main__':
    test()