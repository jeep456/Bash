import pymysql,requests,os,time,glob
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
    info = soup.find('table')
    # links = news.find_all('a')
    # imgages = news.find_all('img')
except:
    print('Ошибка в ответе')

# print(req)
# print(lastFilmsUrl[0])
# print(info)
# print(soup)

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename + ".txt", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename

download_file(lastFilmsUrl[0])


for i in os.listdir('./'):
    if i.endswith(".txt"):
        fileName = i

print(fileName)

# time.sleep(5)

# os.remove(download_file(lastFilmsUrl[0]) + ".txt")
# print(type(download_file(lastFilmsUrl[0])))

# req = requests.get(lastFilmsUrl, headers=headers).text
