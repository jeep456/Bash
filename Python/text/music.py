
data = [i for i in range(1,60)]

data = [str(item).zfill(2) for item in data]

print(data)

# for i in range(1,20):
#     if i % 2 == 0:
#         print(i)

# for i in data:
#     print(type(i))

for i in data:
    if int(i) % 3 == 0:
        print(i)
