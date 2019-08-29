####################################################

###    Скрипт написан на Python 3.6              ###

####################################################

import csv, os, re, requests, helps as hlp
from bs4 import BeautifulSoup
from datetime import datetime
from subprocess import call
import subprocess


url = 'https://lostfilm.tv'                         # Адрес ссылки по которой будем стучаться
req = requests.get(url).text                        # Делаем запрос на адрес и записываем полученный ответ в переменную
soup = BeautifulSoup(req,'lxml')                    # Разбираем полученный ответ с помощью lxml и записываем в переменную
news = soup.find('div',class_='new-movies-block')   # Ищем в ответе блок с новинками и записываем в переменную
links = news.find_all('a')                          # Ищем в блоке ссылки на новинки
imgages = news.find_all('img')                      # Ищем в блоке картинки новинок

titles = []                                         # Заводим пустой массив куда будем добавлять имена новинок
hrefs = []                                          # Заводим пустой массив куда будем добавлять адреса ссылок на новинки
srcs = []                                           # Заводим пустой массив куда будем добавлять адреса картинок на новинки

for i in links:
    titles.append(i.get('title'))                   # Перебираем массив ссылок и выбираем имена новинок в массив titles
    hrefs.append(i.get('href'))                     # Перебираем массив ссылок и выбираем ссылки новинок в массив hrefs

for e in imgages:
    srcs.append(e.get('src'))                       # Перебираем массив картинок и выбираем ссылки каритинок в массив srcs

title = str(titles[1])                              # Выбираем название первой серии из массива и приводим его к строке

episod = repr(hrefs[1])[1:-1]                       # Выбираем ссылку из массива hrefs и извлекаем адрес первой серии

episod = re.search('/episode.*/',episod)            # С помощью регулрки ищем номер серии
episod = episod.group(0)[1:-1]                      # Выбираем совпадение с регуляркой
episod = episod.replace('episode_','Эпизод ')       # Приводим название эпизода к русскому виду

src = "https://" + repr(srcs[0])[3:-1]              # Выбираем адрес картинки первой серии и приводим адрес к строке

imgPath = "/home/jeem/Bash/Python/"+ title +".jpg"  # Заводим переменную с адресом сохранения картинки


# SQL запрос на выборку последней новинки из базы данных
sqlSELECT = "SELECT seria FROM series ORDER BY id DESC LIMIT 1;" # SQL запрос на выборку последней новинки из базы данных

# Делаем запрос в базу и извлекаем название последней новинки
select = subprocess.check_output(['mysql','-N','-uroot','-p123','lars','-e',sqlSELECT]).decode(encoding='utf-8').strip()


# Сравниваем новинку из базы данных и ответом с сайта

if title != select:
    print('Пишем в базу новую серию и выводим popup уведомление')
    call(['wget', '-O', "/home/jeem/Bash/Python/" + title + '.jpg', src])  # Скачиваем картинку для иконки
    call(['notify-send', '-i', imgPath, title])
    # call(['/usr/bin/notify-send', '-i', imgPath, title])
    # call(['/usr/bin/X11/notify-send', '-i', imgPath, title])
    sqlInsert = "INSERT INTO `series` VALUES (NULL,'" + title + "','" + episod + "','" + hlp.today() + "','" + hlp.now() + "','" + hlp.now() + "');"
    call(['mysql', '-uroot', '-p123', 'lars', '-e', sqlInsert])
    # call('/usr/bin/transmission-gtk')
    # call('transmission-gtk')
else:
    print("Пока всё нормально - " + hlp.timeNow())


# Функция очистки файла логов
##########################################################################################################
def delFileError():

    file = '/home/jeem/Bash/Python/errors.txt'

    if os.path.exists(file) & int(hlp.getTimeFormat('H'))%6 == 0 & int(hlp.getTimeFormat('M')) > 55 :
        os.remove(file)

delFileError()
##########################################################################################################