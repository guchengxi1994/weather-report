'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 11:06:42
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-16 11:19:25
'''
import numpy as np
import json
 
 
cityFile = open("D:\\testALg\\weatherreport\\weather-report\\static\\cities.txt","r",encoding='utf8')
cityList = cityFile.readlines()#每一行数据写入到list中

results = []
for i in cityList:
    i = i.replace('label','"label"').replace('name','"name"').replace('pinyin','"pinyin"').replace('zip','"zip"')

    results.append(i)

cityFile.close()

# jso = "".join(results)
# print(jso)

# j = json.loads(jso)
# print(j)