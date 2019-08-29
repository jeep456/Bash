import random,time

rand = random.randrange(0,7)

perm = ('000','001','010','011','100','101','110','111')

ques = {}

for num, i in enumerate(perm):
    ques[num] = i

w = ques[rand]

print(w)

res = int(input())

cnt = 1

while res != rand:
    cnt = cnt + 1
    if cnt > 3:
        print("Попыток больше нет")
        time.sleep(3)
        exit()
    print('Неправильно')
    print("Попытка №" + str(cnt))
    res = int(input())

print("Верный ответ")
