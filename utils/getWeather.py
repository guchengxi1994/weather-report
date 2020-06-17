'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 11:38:21
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-17 11:25:23
'''

import requests
import codecs
import os
from bs4 import BeautifulSoup
import random
from requests.adapters import HTTPAdapter



user_agent = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    ]

# urls = []
site = "https://tianqi.911cha.com/"

def getWeather(day,city='changzhou',infomethod='email'):
    url = site + city
    headers = {'User-Agent': random.choice(user_agent)}
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    response = s.get(url,headers=headers,timeout=3)
    titles = ['日期','时间','气象','天气','温度','湿度','风力','风级','降水量','体感温度','云量']
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        weather_list = soup.select('div[class="mcon noi"] table')
        strs = ''
        for weather in weather_list:
            weather_date = weather.select('tr')[0].getText()
            tr_list = weather.select('tr')
            # print(tr_list)
            res = ''
            flag = False
            for tr in range(0,len(tr_list)):
                td_list= tr_list[tr].select('td')
                th_list=tr_list[tr].select('th')
                
                for t in th_list:
                    if day in t.getText():
                        # print(th.getText())                    
                        # flag = True


                        # str=""
                        # if flag:
                        for th in range(0,len(th_list)):             # 日期
                            res+=th_list[th].getText()+' '
                        
                        res = res + '\n'
                        for td in range(0,len(td_list)):
                            res += titles[td+1]+':'+td_list[td].getText()+" "

                        res = res + '\n'
                        for td in range(0,len(td_list)):
                            res +=  titles[td+1]+':'+tr_list[tr+1].select('td')[td].getText()+" "
            
                    
                        
                        strs = strs + res 

                        break

        
        return strs
                # if i!=0:
                #     print(str+'\n')
                # i+=1
    except TimeoutError:
        return ""

if __name__ == "__main__":
    import datetime

    today = str(datetime.date.today())
    today = datetime.datetime.strptime(today,'%Y-%m-%d').strftime('%m#%d$').replace('#','月').replace('$','日')

    today = today if today[0]!= '0' else today[1:]
    # print(today)
    
    getWeather(today)