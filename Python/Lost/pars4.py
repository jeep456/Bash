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
url = 'https://lostfilm.tv'                             # Адрес ссылки по которой будем стучаться

headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'
    }

try:
    req = requests.get(url,headers=headers).text                        # Делаем запрос на адрес и записываем полученный ответ в переменную
    soup = BeautifulSoup(req, 'lxml')                   # Разбираем полученный ответ с помощью lxml и записываем в переменную
    news = soup.find('div', class_='new-movies-block')  # Ищем в ответе блок с новинками и записываем в переменную
    links = news.find_all('a')                          # Ищем в блоке ссылки на новинки
    imgages = news.find_all('img')                      # Ищем в блоке картинки новинок
except:
    links = []
    imgages = []


titles = []                                         # Заводим пустой массив куда будем добавлять имена новинок
hrefs = []                                          # Заводим пустой массив куда будем добавлять адреса ссылок на новинки
srcs = []                                           # Заводим пустой массив куда будем добавлять адреса картинок на новинки

for i in links:
    titles.append(i.get('title'))                   # Перебираем массив ссылок и выбираем имена новинок в массив titles
    hrefs.append(i.get('href'))                     # Перебираем массив ссылок и выбираем ссылки новинок в массив hrefs

for e in imgages:
    srcs.append(e.get('src'))                       # Перебираем массив картинок и выбираем ссылки каритинок в массив srcs

titles = titles[1:-1]
hrefs = hrefs[1:-1]
titles2 = []
seasones = []
episodes = []
srcs2 = []
novinki = []


needSeries = ['Расскажи мне сказку','Летящие сквозь ночь','Викинги','Побег из Даннеморы','Патриот']

now = "%Y-%m-%d %H:%M:%S"
nows = time.strftime(now)

for i in reversed(titles):
    titles2.append(i)

for i in reversed(hrefs):
    e = re.search('episode.*', i).group(0).replace('episode_','Эпизод ')
    episodes.append(e[:-1])
    try:
        s = re.search('season_[0-9]', i).group(0).replace('season_', 'Сезон ')
        seasones.append(s)
    except Exception:
        seasones.append("Сезон 1")

for i in reversed(srcs):
    srcs2.append(i)

def series(title,season,episode,image,nomb):
    seria = [title[nomb],season[nomb],episode[nomb],image[nomb]]
    return seria

for i in range(10):
    novinki.append(series(titles2,seasones,episodes,srcs2,i))

# def seriaName(val):
#     sqlSeria = "SELECT seria,season,episod FROM series WHERE `seria` = '" + novinki[val][0] +  "' AND `season` = '" + novinki[val][1] + "' AND `episod` = '" + novinki[val][2] + "';"
#     selectCheck = subprocess.check_output(['mysql', '-N', '-uroot', '-p123', 'lars', '-e', sqlSeria]).decode(encoding='utf-8').strip()
#     return selectCheck

def checkSeria(index):
    sqlSelect = "SELECT `seria`, `season`, `episod` FROM `series` WHERE `seria` = '" + novinki[index][0] + "' AND `season` = '" + novinki[index][1] + "' AND `episod` = '" + novinki[index][2] + "' ;"
    cursor.execute(sqlSelect)
    seria = cursor.fetchall()
    return seria

# print(checkSeria(1))

def insertToBase(index):
    sqlInsert = "INSERT INTO `series` VALUES (NULL,'" + novinki[index][0] + "','" + novinki[index][1] + "','" + novinki[index][2] + "','" + time.strftime("%Y-%m-%d") + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "');"
    cursor.execute(sqlInsert)
    dbLars.commit()

# def insertToBase (title,season,episod):
#     sqlInsert = "INSERT INTO `series` VALUES (NULL,'" + title + "','" + season + "','" + episod + "','" + time.strftime("%Y-%m-%d") + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "');"
#     call(['mysql', '-uroot', '-p123', 'lars', '-e', sqlInsert])


# def notify(seria,episode):
#     subprocess.call(['notify-send',seria,episode])
#     subprocess.call(['/usr/bin/notify-send',seria,episode])
#
def telegram (val):
    if val in needSeries:
        print("Send TO TELEGRAM")
     # requests.get('https://api.telegram.org/bot566648079:AAE233AghSpJ9vQyAwrmy77ox7G9-OH6i4Q/sendmessage?chat_id=381581718&text=hello%20my%20friend')

# requests.get('https://api.telegram.org/bot566648079:AAE233AghSpJ9vQyAwrmy77ox7G9-OH6i4Q/sendmessage?chat_id=381581718&text=hello%20my%20friend')


def prosloyka(ind):
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print(novinki[ind])
    print(nows)


if len(checkSeria(0)) == 0 :
    insertToBase(0)
    prosloyka(0)
elif len(checkSeria(1)) == 0 :
    insertToBase(1)
    prosloyka(1)
elif len(checkSeria(2)) == 0 :
    insertToBase(2)
    prosloyka(2)
elif len(checkSeria(3)) == 0 :
    insertToBase(3)
    prosloyka(3)
elif len(checkSeria(4)) == 0 :
    insertToBase(4)
    prosloyka(4)
elif len(checkSeria(5)) == 0 :
    insertToBase(5)
    prosloyka(5)
elif len(checkSeria(6)) == 0 :
    insertToBase(6)
    prosloyka(6)
elif len(checkSeria(7)) == 0 :
    insertToBase(7)
    prosloyka(7)
elif len(checkSeria(8)) == 0 :
    insertToBase(8)
    prosloyka(8)
elif len(checkSeria(9)) == 0 :
    insertToBase(9)
    prosloyka(9)
else:
    # print("Новинок пока нет")
    if os.path.getsize("/home/jeen/Bash/Python/Lost/errors4.txt") > 1000000 :
        os.remove("/home/jeen/Bash/Python/Lost/errors4.txt")





dbLars.close()
