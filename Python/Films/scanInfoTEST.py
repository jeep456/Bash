# Подключаем нужные модули
from bs4 import BeautifulSoup
import pymysql,requests,re
from googlesearch import search
import os.path
from lxml import html
import datetime
from urllib.request import urlopen
# import urllib

# Определяем функцию подключения в серверу mysql
def dbConf(db,cursor=0):
    dbConf = pymysql.connect("localhost","root","123",db)

    if cursor == 1:
        cursor = dbConf.cursor()
        return cursor
    else:
        return dbConf
# Записываем в переменную cursor подключение к бд
cursor = dbConf("films",1)

## Заводим функцию для временной отметки в логах ##
def vremya(val = 0):
    time = datetime.datetime.now().time()
    tm = str(time)
    tm = tm[0:-7]

    if val == 1:
        return tm
    else:
        print(tm)
###################################################

# Пишем sql запрос на выборку из бд id одного фильма без обложки и описания, его имя и год
sql = "SELECT id,name,year FROM `films` WHERE `name_kinopoisk` IS NULL LIMIT 1;"
# Делаем запрос к серверу mysql
cursor.execute(sql)

# Проверяем есть ли фильмы без обложки и описания, и если фильмов нет
# выводим соответствуюзщее уведомление и прерываем действия скрипта.
# Если есть заводим переменную rez и выбираем первый элемент
try:
    rez = cursor.fetchall()[0]
except Exception:
    print('Все фильмы просканированы, ничего не делаем (' + str(vremya(1)) + ")")
    exit()


# Заводим соответствующие переменные
fildId,filmYear  = rez[0],rez[2] # id фильма и его год
# filmYear = rez[2] # Год фильма
# filmName = rez[1] # Имя фильма  ????????????????????????????
filmSearch = rez[1] + " (" + str(rez[2]) + ")" + " Кинопоиск" # Строка для поиска фильма в гугле

print(rez)
print(fildId)
print(filmYear)
# print(filmName)
print(filmSearch)


#### if len(rez) > 0 :
####     print("Запускаем функцию поиска фильма в гугле")
####     filmId = rez[0][0]
####     filmYear = rez[0][4]
####     filmSearch.append(str(rez[0][1]) + " (" + str(rez[0][4]) + ")")
####     print("ID Фильма " + str(filmId))
#### else:
####     print('Все фильмы просканированы, ничего не делаем (' + str(vremya(1)) + ")")
####     exit()
####
#### filmSearch = str(filmSearch[0]) + " кинопоиск"
#### print(filmSearch)


# Делаем запрос в гугл api и выбираем первый пезультат
url = [i[0:-1] for i in search(filmSearch,stop=1)]

print(url)
print(type(url))


##### for url in search(filmSearch,stop=1):
#####     pass
#####
##### url = url[0:-1]
##### print(url)

# Извлекаем из результата поиска с гугла имя фильма на кинопоиске
name_kinopoisk = url[0].replace("https://www.kinopoisk.ru/film/","")

print(name_kinopoisk)

# Проверяем есть ли в имени знак дефис и если есть с помощью регулярок вырезаем имя картинки, если нет то оставляем как есть
if "-" in name_kinopoisk:
     image = str(re.search(str(filmYear) + "-.[0-9]+",name_kinopoisk)[0])
     image = image.replace(str(filmYear) + "-","")
else:
     image = name_kinopoisk

print(image)

# Собираем результаты в кортеж
done = (url,name_kinopoisk,image)

print(done)
# print(done[0])

html = urlopen(done[0])
bsObj = BeautifulSoup(html.read())
print(bsObj)
# resp = html.read()
# resp =resp.decode("UTF-8")



# def grabKinopoisk():
#     html = urlopen(done[0])
#     resp = html.read()
#     resp = resp.decode('UTF-8')
#     return resp
#
# if os.path.isfile("rez.txt"):
#     print('Ничего не делаем')
#     d = open('rez.txt', 'r+')
#     rd = d.read()
#     d.close()
#     # print(rd)
#     scan = html.fromstring(rd)
#     # for i in scan:
#     opisanie = scan.xpath('//div[@itemprop="description"]/text()')
#     # if "\xa0" in opisanie:
#     opisanie = opisanie[0].replace("\xa0", " ")
#     done = done + (opisanie,)
#     os.remove("rez.txt")
# else:
#     resp = grabKinopoisk()
#     if "вашего IP-адреса" in resp:
#         print('Рано')
#     else:
#         # bs = BeautifulSoup(resp)
#         # print(bs)
#         f = open("rez.txt", 'w')
#         f.write(resp)
#         f.close()
#
#
# print(done)
# # / len(done))
# if len(done) > 3:
#     sqlInsert = "UPDATE `films` SET `name_kinopoisk` = '" + str(done[1]) + "', `image` = '" + str(done[2]) +"', `about` = '" + str(done[3]) + "' WHERE `id` = '" + str(filmId) + "'"
#     cursor.execute(sqlInsert)
#     # dbConn.commit()
#     print(sqlInsert)
#
# vremya()
#
#

