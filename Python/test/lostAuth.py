from bs4 import BeautifulSoup

url = "https://lostfilm.tv"

rq = BeautifulSoup.get(url)

print(rq)