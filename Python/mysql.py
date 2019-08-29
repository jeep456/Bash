import MySQLdb
import helps as hlp
from subprocess import call

myCon = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = '123',
    db = 'lars'
)

# cur = myCon.cursor()

# cur.execute("INSERT INTO `series` VALUES (NULL,'Why','45','2018-11-16','null',%s,%s);",(now(),now()))

nameSeria = 'Хуетень'
episod = '900'
imgPath = '/home/'

sql = "INSERT INTO `series` VALUES (NULL,'" + nameSeria + "','" + episod + "','" + hlp.today() + "','" + imgPath + "','" + hlp.now() + "','" + hlp.now() + "');"

call(['mysql','-uroot','-p123','lars','-e',sql])

# print(cur.execute('SELECT * FROM series'))

print(sql)