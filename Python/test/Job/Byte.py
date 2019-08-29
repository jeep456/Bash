import pymysql

# dbConf = ('lars','jobs')
# dbLars = pymysql.connect("localhost","root","123",dbConf[0])
# cursor = dbLars.cursor()

def connect(nameDataBase,localhost = 'localhost',root = 'root',password = '123'):
    dbConn = pymysql.connect("localhost","root","123",nameDataBase)
    return dbConn.cursor()
    # return cursor

cursor = connect('lars')



# sqlApril = "SELECT `hours` FROM `jobs` WHERE `date` LIKE '2019-04-%'"
sqlApril = "SELECT `hours` FROM `jobs` WHERE `id` > 0 AND `id` < 17"
# sqlMay = "SELECT `hours` FROM `jobs` WHERE `date` LIKE '2019-05-%'"
sqlMay = "SELECT `hours` FROM `jobs` WHERE `id` > 16 AND `id` < 48"

sqlIun = "SELECT `hours` FROM `jobs` WHERE `id` > 47 AND `id` < 78"

cursor.execute(sqlApril)
rezApril = cursor.fetchall()

cursor.execute(sqlMay)
rezMay = cursor.fetchall()

cursor.execute(sqlIun)
rezIun = cursor.fetchall()

stavka = 140

aprilHours = []
mayHours = []
iunHours = []

for i in rezApril:
    aprilHours.append(int(i[0]))

for i in rezMay:
    mayHours.append(int(i[0]))

for i in rezIun:
    iunHours.append(int(i[0]))

aprilHours = sum(aprilHours)
aprilSum = stavka*aprilHours

mayHours = sum(mayHours)
maySum = stavka*mayHours

iunHours = sum(iunHours)
iunSum = stavka*iunHours

print("---------------------------------------------------------------------------------")
print("Всего часов за Апрель = " + str(aprilHours) + " часов")
print("Итого за Апрель = " + str(aprilSum) + " руб")

print("---------------------------------------------------------------------------------")
# print(mayHours)
print("Всего часов за Апрель = " + str(mayHours) + " часов")
# print(maySum)
print("Итого за Май = " + str(maySum) + " руб")

print("---------------------------------------------------------------------------------")
# print(mayHours)
print("Всего часов за Июнь = " + str(iunHours) + " часов")
# print(maySum)
print("Итого за Июнь = " + str(iunSum) + " руб")







# april = [16,8,16,16,16,4,16,16,16,8,8,16,16]
#
# may = [16,16,16,16,6,8,16]
#
# hoursApril = sum(april)
# hoursMay = sum(may)
#
# stavka = 150
#
# print("-----------------------------------------------------------------------------------------------------------------")
#
# print("Всего часов за апрель = " + str(hoursApril))
# print("Должно выйти за апрель = " + str(stavka*hoursApril))
#
# print("-----------------------------------------------------------------------------------------------------------------")
#
# print("Всего часов за май = " + str(hoursMay))
# print("Должно выйти за май = " + str(stavka*hoursMay))
#
