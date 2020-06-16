'''
@lanhuage: python
@Descripttion:  https://zhuanlan.zhihu.com/p/36889478
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 10:27:40
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-16 10:28:00
'''
import requests
import codecs
import os
from bs4 import BeautifulSoup
import random

user_agent = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    ]
headers = {'User-Agent': random.choice(user_agent)}
urls = []
a="https://tianqi.911cha.com/"
b=input("请输入要查看的城市：(输入拼音)")
url=a+str(b)
urls.append(url)
print("时间，天气，温度，湿度，风力，风级，降水量，体感温度，云量")
for url in urls:
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_list = soup.select('div[class="mcon noi"] table')
    for weather in weather_list:
        weather_date = weather.select('tr')[0].getText()
        tr_list = weather.select('tr')
        i=0
        for tr in tr_list:
            td_list= tr.select('td')
            th_list=tr.select('th')
            str=""
            for th in th_list:
                str+=th.getText()+'\n'
            for td in td_list:
                str += td.getText()+" "
            if i!=0:
                print(str+'\n')
            i+=1
os.system("pause")