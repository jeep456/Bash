import pymysql

DB = pymysql.connect('localhost','root','123','films')
cursor = DB.cursor()

sql = "SELECT seria,season,episod FROM `series` ORDER BY id DESC LIMIT 10"
# cursor.execute(sql)
cursor.execute("CALL losfilmseries(12)")
result = cursor.fetchall()
serii = []
for i in result:
    print(i)
    serii.append(i[0])

print(result)
print('-------------------------')
print(serii)

DB.close()
