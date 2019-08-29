import pymysql

dbLars = pymysql.connect("localhost", "root", "123", 'films')
cursor = dbLars.cursor()

param = input()

try:
    year = int(param[-5:-1])
    param = param[:-7]
except Exception as e:
    year = 0



# print(year)
# print(type(year))
# print(param)

# name =

def getMovie(value,year):
    # year = int (year)
    if year == 0:
        sql = "SELECT name FROM `films` WHERE name LIKE '%" + value + "%';"
    else:
        year = str(year)
        sql = "SELECT name FROM `films` WHERE name = '" + value + "' AND year = '" + year + "' ;"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
         for e in i:
             # print("Film yeas - " + e)
             result = e
    return result
    # print(sql)

print(getMovie(param,year))


dbLars.close()
