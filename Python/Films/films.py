import os, sys, pymysql

film = input('Введите название фильма')

if len(film) <= 0:
    sys.exit('Error Empty Value')

def mysqlConnect(host,user,pswd,db):
    dbLars = pymysql.connect(host, user, pswd, db)
    cursor = dbLars.cursor()

mysqlConnect('localhost','root','123','films')


def checkFilm(film):
    sql = "SELECT name FROM "

# nameFilm = film.replace(" ","_")

# f = open(nameFilm + '.txt','w+')
# f.write(film)
# f.close()

print(film)
