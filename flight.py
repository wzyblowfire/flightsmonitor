# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:02:31 2019

@author: wzyblowfire
"""

class Flights:
    
    def __init__(self, data_dict):
        self.fid = data_dict['itineraryId'].replace(',', '-')   # 航班号
        self.name = data_dict['flightSegments'][0]['airlineName']   # 航空公司
        dur = data_dict['flightSegments'][0]['duration']   
        hour = int(dur/60)
        minute = dur%60
        self.duration = str(hour)+'h'+str(minute)+'m'   # 行时长
        self.detime = data_dict['flightSegments'][0]['flightList'][0]['departureDateTime']  # 出发时间
        self.decity = data_dict['flightSegments'][0]['flightList'][0]['departureCityName']  # 出发地
        self.arcity = []
        self.artime = []
        for x in data_dict['flightSegments'][0]['flightList']:
            self.arcity.append(x['arrivalCityName'])    # 达到城市（包括中转）
            self.artime.append(x['arrivalDateTime'])    # 达到时间（包括中转）  
        self.price = []
        for x in data_dict['priceList']:
            self.price.append(x['adultPrice']+x['adultTax'])    # 机票价格
        self.minprice = min(self.price)     # 最低价格
        
    def __str__(self):
        # 信息输出
        stri = 'name: ' +self.name+'\n'+\
        'fid: '+self.fid+'\n'+\
        'detime: '+str(self.detime)+' '+str(self.decity)+'\n'+\
        'artime: '+str(self.artime)+' '+str(self.arcity)+'\n'+\
        'duration: '+self.duration+'\n'+\
        'minprice: '+str(self.minprice)
        return stri