import time,datetime
import os,shutil

locale = time.localtime()
day = locale[2]
hour = locale[3]
min = locale[4]

def leadingZero(val):
    if len(str(val)) == 1:
        return "0" + str(val)

def twoDays():
    pathName = "/home/jeen/Bash/tmp/2D/"
    pathName2 = "/home/jeen/sites/lars/resources/views/test/"
    path = os.listdir(pathName)
    # path2 = os.listdir(pathName2)
    dateFile0 = []

    for i in path:
        tm = time.localtime(os.path.getmtime(pathName + i))
        dateFile = dateFile0.append(str(tm.tm_year) + "-" + str(leadingZero(tm.tm_mon)) + "-" + str(tm.tm_mday))

        # print(leadingZero())
        # print(dateFile)
        # print(tm)

    return dateFile0

def now():
    vr = time.localtime()
    now = str(vr.tm_year) + "-" + str(leadingZero(vr.tm_mon)) + "-" + str(vr.tm_mday)
    return now



try:
    # print(now())
    print(twoDays()[0])

    # if (now() > twoDays()[0]:
    # print(now() - twoDays()[0])

except Exception:
    print("Папка пустая")

# print(int(now()) - int(twoDays()[0]))




#
# # Очищаем папку 2D
# if day % 2 == 0:
#     pathName = "/home/jeen/Bash/tmp/2D/"
#     pathName2 = "/home/jeen/sites/lars/resources/views/test/"
#     path = os.listdir(pathName)
#     path2 = os.listdir(pathName2)
#     if len(path) > 0:
#         for i in path:
#             os.remove(pathName + i)
#     if len(path2) > 0:
#         for e in path:
#             os.remove(pathName2 + e)
#
# # Очищаем папку 3H
# if hour % 3 == 0:
#     pathName = "/home/jeen/Bash/tmp/3H/"
#     path = os.listdir(pathName)
#     if len(path) > 0:
#         for i in path:
#             os.remove(pathName + i)
#
# # Очищаем папку 10M
# if min % 10 == 0:
#     pathName = "/home/jeen/Bash/tmp/10M/"
#     path = os.listdir(pathName)
#     if len(path) > 0:
#         for i in path:
#             os.remove(pathName + i)
#
# # Очищаем папку sites/tmp
# if hour > 18 and min < 4:
#     pathName = "/home/jeen/sites/tmp_(everyday)/"
#     path = os.listdir(pathName)
#     print(type(path))
#     if len(path) > 0:
#         for i in path:
#             try:
#                 if os.path.isdir(pathName + i):
#                     shutil.rmtree(pathName + i)
#             except Exception:
#                pass
#
#             try:
#                 os.remove(pathName + i)
#             except Exception:
#                 pass
#




