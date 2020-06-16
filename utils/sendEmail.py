'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 14:45:25
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-16 15:46:39
'''
import smtplib
import os
from .cfg import cfp


def send(sender='',reciver='testsmtp@yeah.net;guchengxi1994@qq.com',message=None):
    try:
        smtpObj = smtplib.SMTP()
        host = cfp.get('email','host')
        user = cfp.get('email','user')
        password = cfp.get('email','password')
        smtpObj.connect(host,25)
        smtpObj.login(user,password)

        smtpObj.sendmail(sender if sender!='' else user,reciver,message.as_string())
        print('发送成功')
    
    except Exception as e:
        print(e)
        
