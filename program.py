'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 10:29:32
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-16 16:07:19
'''
import pypinyin
import sys
import os
import argparse
import configparser
from utils.loadCity import getCityPinyin,getCitys
from utils.MyError import *
from utils.getWeather import getWeather
from utils.cfg import cfp
from utils.sendEmail import send
from email.mime.text import MIMEText
from email.header import Header
import datetime

BASE_DIR = os.path.abspath(os.curdir)
# config_ROOT = BASE_DIR + os.sep + 'static' + os.sep + 'w.ini'
city_ROOT = BASE_DIR + os.sep + 'static' + os.sep + 'cities.txt'
# cfp = configparser.ConfigParser()
# cfp.read(config_ROOT)

citys = getCityPinyin(getCitys(city_ROOT))


if __name__ == "__main__":
    default_city = cfp.get('last-city','city')
    parser = argparse.ArgumentParser(description='weather report')

    parser.add_argument('--day',type=str,default='today')
    parser.add_argument('--city',type=str,default=default_city)
    parser.add_argument('--info',type=str,default='email')

    args = parser.parse_args()

    if not args.day in ['today','tomorrow','yestarday']:
        raise ValueError("param day must in 'today','tomorrow','yestarday' \n other time maybe supported if nessary")

    if args.city and args.city!= default_city:
        city_pinyin_list = pypinyin.lazy_pinyin(args.city)
        city_pinyin = "".join(city_pinyin_list)

        if city_pinyin.capitalize() not in citys:
            raise ValueError("city not found!")
    
    else:
        city_pinyin = default_city

    if args.info not in ['email','sms']:
        raise MethodNotSupportError('your method "{}" not support'.format(args.info))

    print('this city is {}'.format(city_pinyin))

    if args.day == 'today':
        day = str(datetime.date.today())
    elif args.day == 'tomorrow':
        day = str(datetime.date.today()-datetime.timedelta(days=1))
    else:
        day = str(datetime.date.today()+datetime.timedelta(days=1))

    
    
    day = datetime.datetime.strptime(day,'%Y-%m-%d').strftime('%m#%d$').replace('#','月').replace('$','日')
    day = day if day[0]!= '0' else day[1:]
    
    ss = getWeather(day,city=city_pinyin)

        



    message = MIMEText('你好...{}'.format(ss), 'plain', 'utf-8')
    message['From'] = 'testsmtp<{}>'.format(cfp.get('email','user'))
    message['To'] = 'guchengxi<{}>'.format('guchengxi1994@qq.com')

    print(message.as_string())
    send(message=message)
        



