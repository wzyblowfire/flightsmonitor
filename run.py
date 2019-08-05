# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:09:06 2019

@author: win 10
"""
import spider
import time
import traceback
from datetime import datetime
from flight import Flights
import db

for i in range(1000):
    try:
        result = spider.spider_search('2019-09-17')
        flights = {}
        for x in result:
            flight = Flights(x)
            
            flights[flight.fid] = flight
            now_time = datetime.now()
            db.flight_insert(flight, now_time)
        print(flights['AY100-AY1361'])
        print(len(flights))
        
        time.sleep(300)
    except:
        traceback.print_exc()