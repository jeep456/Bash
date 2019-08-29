import os,string
import shutil

alphabet = tuple(string.ascii_letters)

# alphabet = alphabet[:26]

# print(alphabet)

path = "/media/jeen/Transcend/SONG IN MUSIC FROM CONTAKT/LAST BACK FROM CONTACT/"
path2 = "/media/jeen/Transcend/"

# print(os.listdir(path))
songs = sorted(os.listdir(path))

# for i in songs:
#     for l in alphabet:
#         if i in l:
#             print(i)

# for i in songs:
#     print(i[2])

rus = songs[-30:]

# for i in rus:
#     shutil.move(path + i,path2 + i)

# print(rus)
for i in rus:
    print(i)


