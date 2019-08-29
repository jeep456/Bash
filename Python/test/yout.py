from pytube import YouTube
from bs4 import BeautifulSoup
import requests
# YouTube("https://www.youtube.com/watch?v=Q7-bnUckAmk").streams.first().download()

urlChanel = 'https://www.youtube.com/channel/UCdqYirwMU7IhIH3sMMLgFyA';

scan = requests.get(urlChanel).text
soup = BeautifulSoup(scan,'lxml')

a = soup.find('a')

print(a)



