from bs4 import BeautifulSoup
import pymysql,requests,re
from googlesearch import search
import os.path
from lxml import html
import datetime

from urllib.request import urlopen

# def connect(nameDataBase,localhost = 'localhost',root = 'root',password = '123'):
dbConn = pymysql.connect("localhost","root","123","films")
cursor = dbConn.cursor()
# cursor = connect('films')


def updateZnaki():
    sqlUpdate = 'SELECT * FROM `films` WHERE `about` LIKE "%%" OR `about` LIKE "%%"'
    cursor.execute(sqlUpdate)
    print('Апдейтим')

    if len(cursor.fetchall()) > 0:
        sqlUpdate2 = "UPDATE `films` SET `about` = REPLACE(`about`,'',''),`about` = REPLACE(`about`,'','') WHERE `about` LIKE '%%' OR `about` LIKE '%%'"
        cursor.execute(sqlUpdate2)
        dbConn.commit()

#  Функция временной отметки ######################
def vremya(val = 0):
    time = datetime.datetime.now().time()
    tm = str(time)
    tm = tm[0:-7]

    if val == 1:
        return tm
    else:
        print(tm)
###################################################

sql = "SELECT * FROM `films` WHERE `name_kinopoisk` IS NULL LIMIT 1;"
cursor.execute(sql)

rez = cursor.fetchall()
filmSearch = []

if len(rez) > 0 :
    print("Запускаем функцию поиска фильма в гугле")
    filmId = rez[0][0]
    filmYear = rez[0][4]
    filmSearch.append(str(rez[0][1]) + " (" + str(rez[0][4]) + ")")
    print("ID Фильма " + str(filmId))
else:
    print('Все фильмы просканированы, ничего не делаем (' + str(vremya(1)) + ")")
    exit()

filmSearch = str(filmSearch[0]) + " кинопоиск"
print(filmSearch)

for url in search(filmSearch,stop=1):
    pass

url = url[0:-1]
# print(url)
name_kinopoisk = url.replace("https://www.kinopoisk.ru/film/","")

if "-" in name_kinopoisk:
    image = re.search(str(filmYear) + "-.[0-9]+",name_kinopoisk)
    image = str(image[0])
    image = image.replace(str(filmYear) + "-","")
else:
    image = name_kinopoisk

done = (url,name_kinopoisk,image)

print(done)
print(done[0])

def grabKinopoisk():
    html = urlopen(done[0])
    resp = html.read()
    resp = resp.decode('UTF-8')
    return resp

if os.path.isfile("rez.txt"):
    print('Ничего не делаем')
    d = open('rez.txt', 'r+')
    rd = d.read()
    d.close()
    # print(rd)
    scan = html.fromstring(rd)
    # for i in scan:
    opisanie = scan.xpath('//div[@itemprop="description"]/text()')
    # if "\xa0" in opisanie:
    opisanie = opisanie[0].replace("\xa0", " ")
    done = done + (opisanie,)
    os.remove("rez.txt")
else:
    resp = grabKinopoisk()
    if "вашего IP-адреса" in resp:
        print('Рано')
    else:
        # bs = BeautifulSoup(resp)
        # print(bs)
        f = open("rez.txt", 'w')
        f.write(resp)
        f.close()


print(done)
# / len(done))
if len(done) > 3:
    sqlInsert = "UPDATE `films` SET `name_kinopoisk` = '" + str(done[1]) + "', `image` = '" + str(done[2]) +"', `about` = '" + str(done[3]) + "' WHERE `id` = '" + str(filmId) + "'"
    cursor.execute(sqlInsert)
    dbConn.commit()
    print(sqlInsert)


# SELECT * FROM `films` WHERE `about` LIKE "%%" OR `about` LIKE "%%"


updateZnaki()
vremya()



