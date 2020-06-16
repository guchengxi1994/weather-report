'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-06-16 15:01:52
@LastEditors: xiaoshuyui
@LastEditTime: 2020-06-16 15:02:16
'''

import os
import configparser


BASE_DIR = os.path.abspath(os.curdir)
config_ROOT = BASE_DIR + os.sep + 'static' + os.sep + 'w.ini'
city_ROOT = BASE_DIR + os.sep + 'static' + os.sep + 'cities.txt'
cfp = configparser.ConfigParser()
cfp.read(config_ROOT)