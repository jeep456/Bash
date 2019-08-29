



def bes4():
    import csv, os, re, requests, time
    from bs4 import BeautifulSoup
    from datetime import datetime
    from subprocess import call
    import subprocess
    from pytube import YouTube

    url = 'https://lostfilm.tv'                            # Адрес ссылки по которой будем стучаться
    url = "https://www.youtube.com/channel/UCdqYirwMU7IhIH3sMMLgFyA/videos"

    req = requests.get(url).text



    soup = BeautifulSoup(req, 'lxml')
    videos = soup.find("a", class_ = "yt-uix-sessionlink")


    print(videos)



    if os.path.exists("youtube.txt"):
        os.remove("youtube.txt")
        call(['notify-send','-i','software-update-urgent','Файл удалён'])
    else:
        f = open('youtube.txt', 'w+')
        f.write(str(req))
        f.close()


if 1 == 1:
    bes4()
else:
    print(2)

