import requests
from requests.auth import HTTPBasicAuth as auth

url = 'https://lostfilm.tv/me'
# url = 'https://rutracker.org/forum/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
    'From': 'dmitriisinov@mail.ru'
}

# http = requests.get(url)
http2 = requests.get(url, auth = auth('dmitriisinov@mail.ru','dFJpZqRyGb'),headers = headers)

# http = requests.get(url)

def toFile(filename,var):
    f = open(filename,'w')
    f.write(var)
    f.close()

print(http2.status_code)
print(http2.text)
print(http2.headers)

# if http2.status_code == 200:
#     toFile('lostfilm.txt', http2.text)
# else:
#      toFile('lostfilm.txt', http.text)









# read = open(filename).read()

# print(len(http.text))
# print(http.text)

# print(justToFile('lostfilm.txt',http.text))