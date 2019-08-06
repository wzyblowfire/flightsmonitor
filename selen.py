# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:19:27 2019

@author: wzyblowfire
"""
import os
from browsermobproxy import Server 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


url = 'https://flights.ctrip.com/international/search/oneway-hkg0-man?' +\
        'depdate=2019-09-18&cabin=y_s&adult=1&child=0&infant=0'
        
def search_url(depport, arrport, depdate):
    """
    获取携程国际机票搜索的url
    参数：
        depport：出发机场码（机场码可参考data文件夹下的world-airports.csv或
                            访问http://ourairports.com/airports.html下载）
        arrport: 到达机场码
        depdate: 出发日期
    返回值：
        international_url：国际航班搜索url
    """
    international_url = ('https://flights.ctrip.com/international/search/oneway-%s-%s?' + \
                        'depdate=%s&cabin=y_s&adult=1&child=0&infant=0') % (depport, arrport, depdate)
    return international_url

def get_initinfo(url):
    """
    本函数用于获取签名sign信息,transactionID和后续请求data.
    其中使用了selenium和browsermob-proxy.
    其配置安装可见
    参数：
        url: 携程搜索国际航班的url
    返回值：
        sign：后续持续获取航班信息请求头中的签名
        tid: 后续持续获取航班信息请求头中的transactionID
        postdata: 后续持续获取航班信息请求头中的提交json信息
    """
    # browsermob-proxy配置路径，请将这里填写为自己电脑上的路径
    path = os.path.join('D:\code\env', 'browsermob-proxy-2.1.4','bin','browsermob-proxy.bat')   
    server = Server(path)   # 设置服务器脚本路径
    server.start()          
    proxy = server.create_proxy()   # 创建一个浏览器代理
    
    # chrome测试配置
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--disable-gpu')     
    driver = webdriver.Chrome(chrome_options = chrome_options)  # 使用selenium创建浏览器窗口
    proxy.new_har(url, options={'captureContent':True, 'captureHeaders':True})  # 代理服务器开始监测，捕捉文本和请求头信息
    driver.get(url)
    # 显示等待5秒，因为网页会持续加载，需要等待一段时间，直到航空公司内容出现，说明加载成功
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,'airline-name'))) 
    
    result = proxy.har
    
    server.stop()
    driver.quit()
    # 获取https://flights.ctrip.com/international/search/api/search/batchSearch这个访问过程中的重要信息
    for entry in result['log']['entries']:
        if 'batchSearch' in entry['request']['url']:
            postdata = entry['request']['postData']['text']
            header = entry['request']['headers']    
            #flightdata = str(entry['response']['content']).encode('utf-8')
            #print(flightdata)
            for x in header:
                if x['name'] == 'sign':
                    sign = x['value']
                elif x['name'] == 'transactionID':
                    tid = x['value']
                    
    return sign, tid, postdata

if __name__ == '__main__':
    url = search_url('hkg', 'man', '2019-09-20')
    print(get_initinfo(url))