import pymysql
import calendar,datetime
import os

dbLars = pymysql.connect("localhost","root","123","lars")

cursor = dbLars.cursor()

novinka = ["Ориджин","Сезон 1","Эпизод 3"]

# sql = "SELECT * FROM `series` ORDER BY `id` DESC LIMIT 10;"
sqlSelect = "SELECT `seria`, `season`, `episod` FROM `series` WHERE `seria` = '" + novinka[0] + "' AND `season` = '" + novinka[1] + "' AND `episod` = '" + novinka[2] + "' ;"
cursor.execute(sqlSelect)

seria = cursor.fetchall()

dbLars.close()

print(len(seria) == 0)

# bezes = []

# for i in series:
#     bezes.append((i[1],i[2],i[3]))
#
# for i in bezes:
#     print(i[0] + " (" + i[1] + " " + i[2] + ")")
#

day = calendar.day_name

for i in day:
    # print(i)
    pass

drop = ('lars','series')
file = "/home/jeen/Bash/Python/Lost/errors4.txt"

print(os.path.getsize(file))
