import os, re, math

# print(os.name)
# print(os.environ)

files = os.listdir('../')

images = []

for i in files:
    # print(re.search('/.[A-Za-z]*$/g',i))
    print(i)
    # if i.endswith('jpg'):
    #     images.append(i)

# print(images)

# for j in images:
#     print(j)



# def translyator(vel,val):
#
#     if vel == 'f':
#         print(math.ceil((9/5) * val) + 32)
#     elif vel == 'c':
#         print(math.ceil((val - 32)*(5/9)))
#         print(int((val - 32)*(5/9)))
#         print((val - 32)*(5/9))
#     else:
#         print('Empty')

# translyator('c',int(input()))


    # print(i.endswith('jpg'))