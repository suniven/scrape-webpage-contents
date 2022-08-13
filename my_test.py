import os
import re
import time
import lxml
import requests
from seleniumwire import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import and_, asc, desc, or_
from common.model import WebpageInfo
import common.logger as logger
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

#
# options = webdriver.ChromeOptions()
# prefs = {
#     "profile.managed_default_content_settings.images": 1,
# }
# options.add_experimental_option('prefs', prefs)
# #
# # # 方法1
# # # capabilities = DesiredCapabilities.CHROME
# # # capabilities['loggingPrefs'] = {"performance","all"}
# # # self.driver = webdriver.Chrome(
# # #     desired_capabilities=capabilities
# # # )
# #
# # 方法2
# options.add_experimental_option("excludeSwitches", ['enable-automation'])  # window.navigator.webdriver设置为undefined，逃过网站的防爬检查,headless无效
# desired_capabilities = options.to_capabilities()  # 将功能添加到options中
# desired_capabilities['loggingPrefs'] = {
#     "performance": "ALL"  # 添加日志
# }
# driver = webdriver.Chrome(
#     desired_capabilities=desired_capabilities
# )
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# try:
#     url = 'https://t.co/GMu9zd5Q2V'
#     driver.get(url)
#     print(driver.get_log('performance'))
#     print('-' * 60)
#     print(driver.get_log('performance'))
#     for entry in driver.get_log('performance'):
#         params = json.loads(entry.get('message')).get('message')
#         print(params.get('request'))  # 请求连接 包含错误连接
#         print(params.get('response'))  # 响应连接 正确有返回值得连接
# except:
#     print("Error")
# finally:
#     driver.close()
#     driver.quit()

options = {
    'proxy': {
        'http': 'http://127.0.0.1:10809',
        'https': 'http://127.0.0.1:10809',
    }
}
driver = webdriver.Chrome(seleniumwire_options=options)
driver.maximize_window()
driver.implicitly_wait(15)

try:
    driver.get('https://t.co/GMu9zd5Q2V')
    print("---Load Successfully---")
    time.sleep(2)
    # Access requests via the `requests` attribute
    for request in driver.requests:
        if request.response:
            if int(request.response.status_code / 100) == 3:  # 301 302 303 307 308
                print(
                    request.url,
                    request.response.status_code,
                    request.response.headers['location'],
                    # request.response.headers['Content-Type']
                )
except:
    print("...")
finally:
    driver.close()
    driver.quit()
    print("?")