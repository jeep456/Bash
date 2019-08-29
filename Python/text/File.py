# import smtplib

x = lambda y,x = 10: print(x * y)

'''
Важно понимать что это всё делалось на скорую руку и 
некоторые моменты могут быть не такими какими они должны быть
'''

# x(2,9)

# print(type(print()))

# print(int(5**3))

# for i in [1,2..10,]:
#     print(i)

# f = open("file.txt",'r')
# file = f.read().split("\n")
# f.close()
#
# for i in file:
#     print(i)
#
# print(file[9])
#


# 1. Вводим в инпут первый раз - это у нас строка
# 2.
# 3.
# 4.




x = input('Введи число ')

def checkInt(x):
    while True:
        try:
            x = int(x) * 1
            if isinstance(x, int): break
        except Exception:
            x = input('Введи именно число ')
    return x

x = checkInt(x)

print("Конец")
print(x)
print(type(x))

# try:
#     x = int(x)
# except Exception:
#
#     while isinstance(x, int):
#         x = input("Введите именно число ")
#         x = int(x)
#     else:
#         print("This is numeric")



# print(isinstance(x,int))

# try:
    # y = x * 50
# except Exception:
    # x = input()

# while not isinstance(x, int):
    # print("NUMBERIC")
    # x *= 1
    # if isinstance(x, int):
    # x = int(input("Введите именно число "))s

# print(isinstance(x, int))

# while not isinstance(int(x), int):
    # try:
    #     x *= 1
    #     print("This L- " + str(x))
    #     if isinstance(x, int): break
    # except Exception:
    #     print(Exception.args.__init__())
    #     print(type(x))
        # print("Введите именно число")
    # x = input('Введи именно число ')
# else:
#     print("This OK")




# def checkInt(x):
#     while x is not int:
#         try:
#             x *= 1
#             if isinstance(x, int): break
#         except Exception:
#             # print(Exception.args.__init__())
#             # print(type(x))
#             # print("Введите именно число")
#             x = input('Введи именно число ')
#     else:
#         return x



# y = checkInt(x)
#
# print("Число из функции - " + str(y))
# print(type(y))
