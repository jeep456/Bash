import os
import subprocess
import pymysql

files = os.listdir()

print(files)

# if "shut.txt" in files:
#     print("Читаем файл для выключения")
# else:
#     print("Ничего делать не нужно. Файла нет")

dbConn = pymysql.connect("localhost","root","123","lars")
cursor = dbConn.cursor()

sql = "SELECT shut FROM shuts ORDER BY id LIMIT 1"

cursor.execute(sql)
res = cursor.fetchall()

if res[0][0] == 1:
    print("Shutdown")
    # subprocess.run(['init','0'])
else:
    print("NOT Shutdown")

# for i in range(1,50):
#     if i < 10:
#         print("0" + str(i))
#     print("%0" % i)


