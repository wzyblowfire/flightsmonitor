# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:19:27 2019

@author: win 10
"""

import os
from browsermobproxy import Server 
import time
base_url='https://blog.csdn.net/'

url = 'https://flights.ctrip.com/international/search/oneway-hkg0-man?depdate=2019-09-18&cabin=y_s&adult=1&child=0&infant=0'

path = os.path.join('D:\code\env', 'browsermob-proxy-2.1.4','bin','browsermob-proxy.bat')
server = Server(path)
server.start()
proxy = server.create_proxy()



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
chrome_options.add_argument('--disable-gpu')
 
#chrome_driver = r'<path-to-chromedriver.exe>\chromedriver.exe'
 
driver = webdriver.Chrome(chrome_options = chrome_options)
proxy.new_har(url, options={'captureContent':True, 'captureHeaders':True})
driver.get(url)
time.sleep(6)
result = proxy.har


for entry in result['log']['entries']:
   if 'batchSearch' in entry['request']['url']:
        header = entry['request']['headers']
        data = entry['response']['content']
  
print(header)

for x in header:
    if x['name'] == 'sign':
        sign = x['value']
    elif x['name'] == 'transactionID':
        tid = x['value']
        
print(sign, tid)
server.stop()
driver.quit()
