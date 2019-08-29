import telegram
import pymysql
from parse_it import ParseIt
import asyncio

parser = ParseIt()

class Person:

    # model = 100
    # tok = 200

    def nota(self,b,y=2):
        return b**y



# klass = Person()


# print(klass.model)
# print(klass.tok)

print(Person.nota(10,3))

folc = {i for i in range(10)}

# print(folc)
print("********************************************************************",end="\n")

print(folc)

print("********************************************************************")

help(asyncio)
# if klass.model < 500:
#     klass.model,klass.tok = klass.tok,klass.model
#     print(klass.model)
#     print("Есть обмен")












