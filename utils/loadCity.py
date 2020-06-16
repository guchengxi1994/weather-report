'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 11:01:47
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-16 11:24:56
'''

import json

def getCitys(filePath):
    with open(filePath,'r',encoding='utf8') as f:
        cityList = f.readlines()#每一行数据写入到list中

        results = []
        for i in cityList:
            i = i.replace('label','"label"').replace('name','"name"').replace('pinyin','"pinyin"').replace('zip','"zip"')

            results.append(i)
    
    return json.loads("".join(results))

def getCityPinyin(s):
    # py = set()
    py = [x.get('pinyin') for x in s]
    return py



if __name__ == "__main__":
    s = getCitys("D:\\testALg\\weatherreport\\weather-report\\static\\cities.txt")
    # print(s)
    print(getCityPinyin(s))