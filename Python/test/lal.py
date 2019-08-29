import json

f = open('lal.txt','r')

l = []

for i in f:
    print(i, end = '')
    l.append(i[0:-1])

print(l)
