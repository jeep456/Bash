####################################################

###    Скрипт написан на Python 3.6              ###

####################################################

import csv, os, re, requests, time
from bs4 import BeautifulSoup
from datetime import datetime
# from subprocess import call
# import subprocess
import pymysql

# Конфиг ('База Данных','Таблица')
dbConf = ('films','series')
dbLars = pymysql.connect("localhost","root","123",dbConf[0])
cursor = dbLars.cursor()



def needSeries():
    sql = "SELECT `seria` FROM `need_series` ORDER BY `id`"
    cursor.execute(sql)
    results = cursor.fetchall()
    series = []
    for i in results:
        for e in i:
            series.append(e)
    return series

seria = 'Викинг0и'

if seria in needSeries():
    print("УРА ЕСТЬ СЕРИЯ, ШЛЁМ В ТЕЛЕГРАМ")



print(type(needSeries()[0]))
print(needSeries())





# def checkSeria(index):
#     sqlSelect = "SELECT `seria`, `season`, `episod` FROM `series` WHERE `seria` = '" + novinki[index][0] + "' AND `season` = '" + novinki[index][1] + "' AND `episod` = '" + novinki[index][2] + "' ;"
#     cursor.execute(sqlSelect)
#     seria = cursor.fetchall()
#     return seria

# print(checkSeria(1))




dbLars.close()
