import random
import time

count = input("Сколько примеров будем рещшать ? ")

def Primer():
    first = random.randrange(11, 20)

    second = random.randrange(11, 20)

    primer = str(first) + "x" + str(second) + "="

    rezult = first * second

    # print("Результат - " + str(rezult))
    print(primer)

    otvet = input()

    popytka = 0

    # if otvet == rezult:
    #     print("Правильно")
    while int(otvet) != rezult:
        popytka += 1
        if popytka > 2:
            print("Вы проиграли")
            exit()
        print("Ошибка, попробуйте снова")
        otvet = input("")
    else:
        print("Правильно. Вы выиграли")


for i in range(0,int(count)):
    Primer()
    time.sleep(2)
