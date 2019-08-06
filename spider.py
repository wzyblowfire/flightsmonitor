# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:37:55 2019

@author: win 10
"""
import requests
import json
import pandas as pd
from lxml import etree

index_time = 'time'
index_url = 'url'
index_sign = 'sign'
index_tid = 'transactionid'

def get_info(time='2019-09-17'):
    path = '.\data\query.xlsx'
    info = pd.read_excel(path, 'Sheet1', encoding = 'uft-8').fillna('')
    return info
    
def spider_searchcriteria(URL):
    #URL = "https://flights.ctrip.com/international/search/oneway-hkg0-man?depdate=2019-09-17&cabin=y_s&adult=1&child=0&infant=0"
    response = requests.get(URL)
    
    html = etree.HTML(response.text)
   
    if 'GlobalSearchCriteria ' in response.text:
        print(1)
    node  = html.xpath(' /html/head/script[3]/text()')
    #print(node_list)
    stri =node[0].replace(';','').replace(' ','').replace('GlobalSearchCriteria=','')
    sc = json.loads(stri)
    return sc
    
def spider_searchflights(sign, tid, post_data):
    search_URL = 'https://flights.ctrip.com/international/search/api/search/batchSearch?v='
    #sc = spider_searchcriteria(URL)
    #sc['flightWayEnum'] = "OW"
    #sc['transactionid'] = tid
    #data = json.dumps(post_data)
    #print(data)
    headers = {
    'authority': 'flights.ctrip.com',
    'method': 'POST',
    #'path': '/international/search/api/search/batchSearch?',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '906',
    'content-type': 'application/json;charset=UTF-8',
    'cache-control': 'no-cache',
    #'cookie': 'abtest_userid=842bc892-b18c-429c-a447-e38ffe16af34; gad_city=31f35a60e938dff697ddea628b5bea7c; _RF1=183.14.31.46; _RSG=4rK6_c0QLdBbuq7EofSak8; _RDG=28d695dddc4bdc27611bd8922b97f88002; _RGUID=b9d56809-bf19-4d44-8ba4-729c8e1f4e25; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _ga=GA1.2.1422953371.1564113616; _gid=GA1.2.1650754753.1564113616; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&Expires=1564718416203; DomesticUserHostCity=SZX|%c9%ee%db%da; MKT_Pagesource=PC; appFloatCnt=2; FlightIntl=Search=[%22HKG|%E9%A6%99%E6%B8%AF(%E9%A6%99%E6%B8%AF%E5%9B%BD%E9%99%85%E6%9C%BA%E5%9C%BA)(HKG)|58|HKG|HKG|480%22%2C%22MAN|%E6%9B%BC%E5%BD%BB%E6%96%AF%E7%89%B9(MAN)|722|MAN|60%22%2C%222019-09-17%22]; _jzqco=%7C%7C%7C%7C1564113619801%7C1.994656999.1564113616249.1564113652387.1564113669406.1564113652387.1564113669406.undefined.0.0.5.5; __zpspc=9.1.1564113616.1564113669.5%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfi=p1%3D10320672927%26p2%3D10320672927%26v1%3D6%26v2%3D5; _bfa=1.1563519570023.2h1ny1.1.1563519570023.1564113613258.2.7; _bfs=1.6; _gat=1',
    'origin': 'https://flights.ctrip.com',
    'pragma': 'no-cache',
    #'referer': 'https://flights.ctrip.com/international/search/oneway-hkg0-man?depdate=2019-09-17&cabin=y_s&adult=1&child=0&infant=0',
    'sign': sign,
    #'transactionid': sc['transactionID'],
    'transactionid': tid,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.66 Safari/537.36'
    }
    
    response = requests.post(search_URL, data=post_data, headers=headers)

    dict_json = json.loads(response.text)
    if dict_json['status'] != 0:
        print(dict_json['msg'])
    return dict_json

def spider_search(time):
    info = get_info()
    info_ = info[info[index_time] == time].reset_index(drop=True)
    #print(print(info_))
    print(info_[index_url])
    URL = info_[index_url][0]
    sign = info_[index_sign][0]
    tid = info_[index_tid][0]
    result = spider_searchflights(URL, sign, tid)
    print(len(result['data']['flightItineraryList']))
    return result['data']['flightItineraryList']
    
    
