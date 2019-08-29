import os


dictionary = {"one":"Слон","two":"Бегемот","tri":"Лев","fore":"Зебра",}

duo = "Слон"

if 1:
    # print("Правда")
    pass
else:
    # print("Ложь")
    pass

for i in dictionary:
    # print(dictionary[i])
    if duo in dictionary[i]:
        print("Есть контакт")
    else:
        print("Облом")

print(os.getcwd())
