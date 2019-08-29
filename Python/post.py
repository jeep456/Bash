import requests

url = 'https://lostfilm.tv'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

req = requests.get(url,headers = headers)

f = open('lost.html','w')
f.write(repr(req.content))
f.close()