# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:02:31 2019

@author: win 10
"""

class Flights:
    
    def __init__(self, data_dict):
        self.fid = data_dict['itineraryId'].replace(',', '-')
        self.name = data_dict['flightSegments'][0]['airlineName']
        dur = data_dict['flightSegments'][0]['duration']
        hour = int(dur/60)
        minute = dur%60
        self.duration = str(hour)+'h'+str(minute)+'m'
        self.detime = data_dict['flightSegments'][0]['flightList'][0]['departureDateTime']
        self.decity = data_dict['flightSegments'][0]['flightList'][0]['departureCityName']
        
        self.arcity = []
        self.artime = []
        for x in data_dict['flightSegments'][0]['flightList']:
            self.arcity.append(x['arrivalCityName'])
            self.artime.append(x['arrivalDateTime'])
        self.price = []
        for x in data_dict['priceList']:
            self.price.append(x['adultPrice']+x['adultTax'])
        self.minprice = min(self.price)
        
    def __str__(self):
        stri = 'name: ' +self.name+'\n'+\
        'fid: '+self.fid+'\n'+\
        'detime: '+str(self.detime)+' '+str(self.decity)+'\n'+\
        'artime: '+str(self.artime)+' '+str(self.arcity)+'\n'+\
        'duration: '+self.duration+'\n'+\
        'minprice: '+str(self.minprice)
        return stri