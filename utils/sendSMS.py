'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-17 10:26:08
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-17 10:44:19
'''
from twilio.rest import Client
from .cfg import cfp

def sendSMS(message,phoneNumber):
    account_sid = cfp.get('sms','sid')
    auth_token = cfp.get('sms','token')

    client = Client(account_sid,auth_token)

    message = client.messages.create(
        to=phoneNumber,
        from_='+12058902585',
        body=message
    )

    print(message.sid)

if __name__ == "__main__":
    sendSMS("hello","+86xxxxxxxxxx")