import hashlib, uuid

password = "KEY"

salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password + salt).hexdigest()

print(hashed_password)
# print(datetime.now().timetuple().tm_yday)

# print(calendar.iterweekdays())

# print(calendar.LocaleHTMLCalendar(locale='Russian_Russia'))

# for i in range(2019,1909,-1):
#     if calendar.isleap(i):
#         print("Этот год считается высокосным - " + str(i))

# def season(i):
#     if i != 0 and i < 3 or i == 12:
#         print("Это зима")
#     elif i > 2 and i < 6:
#         print("Это весна")
#     elif i > 5 and i < 9:
#         print("Это лето")
#     elif i > 8 and i < 12:
#         print("Это осень")
#     elif i == 0:
#         print("Нет такого месяца")
#     else:
#         print("Нет такого месяца")
#
# season(5)

# n = 15
#
# for i in range(1,n + 1):
#     for b in range(1,i - 1):
#         print("*",sep="",end="")
#     print("")

# # Сумма вклада
# a = 15000
#
# def Vklad(x):
#     p = int(x/10)
#     for i in range(1,11):
#         x += p
#     print(x)
#
#     # d = [int(o) for o in range(1,11)]
#     # print(len(d))
#
# Vklad(a)

# vark = 200
#
# # if x >= 1 & x % 1 == 0:
# #     print(vark)
#
# def IsPrime(n):
#    d = 2
#    while d * d <= n and n % d != 0:
#        d += 1
#    return d * d > n
#
# for i in range(1,vark):
#     if IsPrime(i):
#         print(i)
