import pymysql,requests
from bs4 import BeautifulSoup


dbFilms = pymysql.connect("localhost","root","123","films")
cursor = dbFilms.cursor()

def getLast():
    sql = "SELECT `film_id`,`genre_id` FROM `fimls_genres` GROUP BY `film_id` ;"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

last = getLast()[-1]

# for i in res:
    # print(i)
    # pass
    # last.append(i[-1])

# print(res)

def getFilms(last):
    sql = "SELECT * FROM `films` LIMIT " + str(last) + ", 1 ;"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

lastFilms =  getFilms(last[0])

lastFilmsId = []
lastFilmsUrl = []

for i in lastFilms:
    # print(i[0])
    # lastFilmsId.append(i[2])
    lastFilmsUrl.append("https://www.kinopoisk.ru/film/" + i[2])


# print(lastFilmsUrl[0])

headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'
    }

try:
    # req = requests.get(lastFilmsUrl[0], headers=headers).text
    session = requests.Session()
    req = session.get(lastFilmsUrl[0],headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    info = soup.find('div', class_='shadow')
    # links = news.find_all('a')
    # imgages = news.find_all('img')
except:
    print('Ошибка в ответе')


print(soup)

# req = requests.get(lastFilmsUrl, headers=headers).text
