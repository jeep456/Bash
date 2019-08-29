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

titles = titles[1:-1]
hrefs = hrefs[1:-1]
titles2 = []
hrefs2 = []
srcs2 = []


for i in reversed(titles):
    titles2.append(i)

for i in reversed(hrefs):
    i = re.search('episode.*', i).group(0).replace('episode_','Эпизод ')
    hrefs2.append(i[:-1])

for i in reversed(srcs):
    srcs2.append(i)

def series(title,href,image,nomb):

    seria = [title[nomb],href[nomb],image[nomb]]
    return seria

# eps =

# for i in eps:
#     print(i)

novinki = []

for i in range(10):
    novinki.append(series(titles2,hrefs2,srcs2,i))

for i in novinki:
    # print(i[0] + " " + i[1])
    pass




# SQL запрос на выборку последней новинки из базы данных
sqlName = "SELECT seria FROM series ORDER BY id DESC LIMIT 1;" # SQL запрос на выборку последней новинки из базы данных
sqlEpisode = "SELECT episod FROM series ORDER BY id DESC LIMIT 1;" # SQL запрос на выборку последней новинки из базы данных

# Делаем запрос в базу и извлекаем название последней новинки
# mysql_config_editor set --login-path=proftpd --host=localhost --user=root --password=123
# selectConf = subprocess.call(['mysql_config_edito','set','--login-path=proftpd','--host=localhost','--user=root','--password=123'])
selectName = subprocess.check_output(['mysql','-N','-uroot','-p123','lars','-e',sqlName]).decode(encoding='utf-8').strip()
selectEpisod = subprocess.check_output(['mysql','-N','-uroot','-p123','lars','-e',sqlEpisode]).decode(encoding='utf-8').strip()

seriaFromBase = selectName + " " + selectEpisod
# seriaFromLost = novinki[0][0] + " " + novinki[0][1]

# print(seriaFromLost)

# print(seriaFromBase == seriaFromLost)

def insertToBase (title,episod):
    sqlInsert = "INSERT INTO `series` VALUES (NULL,'" + title + "','" + episod + "','" + hlp.today() + "','" + hlp.now() + "','" + hlp.now() + "');"
    call(['mysql', '-uroot', '-p123', 'lars', '-e', sqlInsert])

def seriaFromLost(cnt):
    return novinki[cnt][0] + " " + novinki[cnt][1]
    # if seriaFromBase != seriaFromLost:

# print(seriaFromLost(0))

def seriaCheckBase(novinki):
    sqlSeriaCheck = "SELECT `seria`, `episod` FROM `series` WHERE `seria` = '" + novinki[0] + "' AND `episod` = '" + novinki[1] + "';"
    # subprocess.call(['mysql_config_editor','set', '--login-path=local', '--host=localhost', '--user=root','--password=123'])
    selectSeriaCheck = subprocess.check_output(['mysql', '-N', '-uroot', '-p123', 'lars', '-e', sqlSeriaCheck]).decode(encoding='utf-8')
    return selectSeriaCheck

def notify(seria,episode):
    subprocess.call(['notify-send',seria,episode])

# print(len(seriaCheckBase(novinki[4])) == 0)
if len(seriaCheckBase(novinki[0])) == 0 :
    cnt = 0
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[1])) == 0:
    cnt = 1
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[2])) == 0:
    cnt = 2
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[3])) == 0:
    cnt = 3
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[4])) == 0:
    cnt = 4
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[5])) == 0:
    cnt = 5
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[6])) == 0:
    cnt = 6
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[7])) == 0:
    cnt = 7
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[8])) == 0:
    cnt = 8
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
elif len(seriaCheckBase(novinki[9])) == 0:
    cnt = 9
    insertToBase(novinki[cnt][0], novinki[cnt][1])
    notify(novinki[cnt][0], novinki[cnt][1])
else:
    print("Пока новинок нет")


# Делаем запрос в базу и извлекаем название последней новинки
# mysql_config_editor set --login-path=proftpd --host=localhost --user=root --password=123
# selectConf = subprocess.call(['mysql_config_edito','set','--login-path=proftpd','--host=localhost','--user=root','--password=123'])
# selectNameCheck = subprocess.check_output(['mysql','-N','-uroot','-p123','lars','-e',sqlName]).decode(encoding='utf-8').strip()
# selectEpisodCheck = subprocess.check_output(['mysql','-N','-uroot','-p123','lars','-e',sqlEpisode]).decode(encoding='utf-8').strip()

# seriaFromBaseCheck = selectName + " " + selectEpisod

# Сравниваем новинку из базы данных и ответом с сайта
#
# if title != select:
#     print('Пишем в базу новую серию и выводим popup уведомление')
#     call(['wget', '-O', "/home/jeem/Bash/Python/" + title + '.jpg', src])  # Скачиваем картинку для иконки
#     call(['notify-send', '-i', imgPath, title])
#     call(['/usr/bin/notify-send', '-i', imgPath, title])
#     call(['/usr/bin/X11/notify-send', '-i', imgPath, title])
#     sqlInsert = "INSERT INTO `series` VALUES (NULL,'" + title + "','" + episod + "','" + hlp.today() + "','" + hlp.now() + "','" + hlp.now() + "');"
#     call(['mysql', '-uroot', '-p123', 'lars', '-e', sqlInsert])
#     call('/usr/bin/transmission-gtk')
#     call('transmission-gtk')
# else:
#     print("Пока всё нормально - " + hlp.timeNow())
#
#
# Функция очистки файла логов
#########################################################################################################
# def delFileError():
#
#     file = '/home/jeem/Bash/Python/errors.txt'
#
#     if os.path.exists(file) & int(hlp.getTimeFormat('H'))%6 == 0 & int(hlp.getTimeFormat('M')) > 55 :
#         os.remove(file)
#
# delFileError()
#########################################################################################################
#