# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:14:14 2019

@author: win 10
"""
import requests
def search_url():
    import pandas as pd
    airports_data = pd.read_csv('.\data\world-airports.csv', encoding = 'utf-8').fillna('')
    print(airports_data['iata_code'])
    url = ''
    return url


#search_url()
getcity_url = 'https://flights.ctrip.com/international/search/restapi/soa2/15095/json/flightCityPageData?v='

 #dict_json = json.loads(response.text)
 
headers = {
'authority': 'flights.ctrip.com',
'scheme': 'https',
'method': 'POST',
#'path': '/international/search/restapi/soa2/15095/json/flightCityPageData?v=0.8918057437954641',
'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-length': '20',
'content-type':'application/json;charset=UTF-8',
'pragma': 'no-cache',
#'cookie': '_abtest_userid=842bc892-b18c-429c-a447-e38ffe16af34; _RSG=4rK6_c0QLdBbuq7EofSak8; _RDG=28d695dddc4bdc27611bd8922b97f88002; _RGUID=b9d56809-bf19-4d44-8ba4-729c8e1f4e25; _ga=GA1.2.1422953371.1564113616; MKT_Pagesource=PC; login_uid=2F311DCACD029AD74748F12C78480A0A; login_type=0; UUID=3F41E5838F194E0488DBD32CE4B61E1B; IsPersonalizedLogin=F; StartCity_Pkg=PkgStartCity=30; MKT_OrderClick=ASID=48977981809486398596839807782&AID=4897&CSID=798180&OUID=&CT=1564561341243&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D798180%26allianceid%3D4897%26bd_vid%3D9486398596839807782&VAL={"pc_vid":"1563519570023.2h1ny1"}; FD_SearchHistorty={"type":"S","data":"S%24%u65E0%u9521%28WUX%29%24WUX%242019-09-09%24%u6DF1%u5733%28SZX%29%24SZX"}; Session=SmartLinkCode=U1955227&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; Union=OUID=&AllianceID=1068271&SID=1955227&SourceID=&Expires=1565313696139; _gid=GA1.2.2037639694.1564967553; FlightIntl=Search=[%22HKG|%E9%A6%99%E6%B8%AF(HKG)|58|HKG|480%22%2C%22MAN|%E6%9B%BC%E5%BD%BB%E6%96%AF%E7%89%B9(MAN)|722|MAN|60%22%2C%222019-09-17%22]; _RF1=183.14.133.80; _gat=1; _jzqco=%7C%7C%7C%7C1565055529155%7C1.994656999.1564113616249.1565055931873.1565058799969.1565055931873.1565058799969.undefined.0.0.77.77; __zpspc=9.16.1565058799.1565058799.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23; appFloatCnt=12; gad_city=31f35a60e938dff697ddea628b5bea7c; _bfa=1.1563519570023.2h1ny1.1.1565055526104.1565058797101.16.111; _bfs=1.2; _bfi=p1%3D10320672927%26p2%3D10320669438%26v1%3D111%26v2%3D110',
'origin': 'https://flights.ctrip.com',
#'transactionid': 'fb107b34527b462da3fef05ebf7ced51',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.66 Safari/537.36'
}
response = requests.post(getcity_url, headers=headers)
print(response.text)