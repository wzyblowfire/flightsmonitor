# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:26:04 2019

@author: Eric
"""

import pymysql
#from flight import Flights

def Db():
    ip = '127.0.0.1'
    port = 3306
    user = 'root'
    pw = 'a728722551'
    database = 'flights'
    connection = pymysql.connect(host=ip, port=port, user=user , password=pw, db=database,  
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)   
    return connection


connection = Db()
#设置top值
def flight_insert(flight, now_time):
    conn = Db()
    cursor = conn.cursor()
    table = 'search_1'

    sql = "INSERT INTO " + table + " (fid, airline, detime, decity, artime, arcity, duration, minprice, uptime)" + \
            " VALUES( %(fid)s, %(airline)s, %(detime)s, %(decity)s, %(artime)s, %(arcity)s, %(duration)s, %(minprice)s, %(uptime)s)"
    value = {
            #"table":table,
            "fid": flight.fid,
            "airline": flight.name,
            "detime": flight.detime,
            "decity": flight.decity,
            "artime": flight.artime[-1],
            "arcity":   flight.arcity[-1],
            "duration": flight.duration,
            "minprice": str(flight.minprice),
            "uptime": str(now_time)
            }
    print(value)
    print(cursor.execute(sql, value))
    
    
    #INSERT INTO `flights`.`search_1` (`fid`, `airline`, `detime`, `artime`, `decity`, `arcity`, `duration`, `minprice`, `uptime`) VALUES ('11', '1', '2019-08-04 18:04:45', '2019-08-04 18:04:46', '11', '11', '11', '11', '2019-08-04 18:04:52');
    conn.commit()