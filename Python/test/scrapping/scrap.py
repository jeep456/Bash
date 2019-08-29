# import google
# from googlesearch import search
#
# sea = "Славные парни (2016) кинопоиск"
#
# for url in search(sea,stop=1):
#     print(url)

from urllib.request import urlopen

html = urlopen('http://jeep-rap.ru/')
html = html.encode(encoding='UTF-8',errors='strict')
print(html.read())
