import pymysql

dbCon = pymysql.connect(
    'localhost','root','123','phones'
)

cursor = dbCon.cursor()

sql = "SELECT * FROM humans;"

cursor.execute(sql)

resp = cursor.fetchall()

print(resp[0][1] + " " + resp[0][2])
