# /usr/bin/env python
from twilio.rest import Client
import config as cfg

global numbers, account_sid, auth_token

twilioNumber = cfg.configuration['twilioNumber']
station = cfg.configuration['stationNumber']
master = cfg.master

# Find these values at https://twilio.com/user/account
account_sid = cfg.configuration['account_sid']
auth_token = cfg.configuration['twilio_auth_Token']

client = Client(account_sid, auth_token)

def send(text,number,keyword):
    context = "Keyword: %s Context: %s Call this number to win %s" % (keyword.upper(),text, station,)
    client.api.account.messages.create(
    to=number,
    from_=twilioNumber,
    body=context)
    client.api.account.messages.create(
    to=master,
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

def sendToMaster(text):
    client.api.account.messages.create(
    to=master,
    from_=twilioNumber,
    body="Program is running %s" % text)


if __name__ == '__main__':
    test()