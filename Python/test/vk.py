import requests
from bs4 import BeautifulSoup
import json, re


# https://vk.com/friends?id=section=all

TOKEN = "941789dfa99e1a399057b7684c1a01be857b757de340049639ca22cbea5974ab69041fcf8f906f803ced4"
url = "https://api.vk.com/method/friends.get?user_id=81895691&v=5.52&access_token=" + TOKEN

req = requests.get(url).text

friends = json.loads(req)["response"]["items"]

def getUserName(idUser,typeName = ''):

    userId = idUser

    if not isinstance(idUser,str):
        userId = str(idUser)

    friendName = requests.get('https://vk.com/id' + userId).text
    soup = BeautifulSoup(friendName, 'lxml')
    find = soup.findAll('title')
    find = re.search("<title>(.*?)</title>", str(find[0])).group(1)
    find = find.replace(" | ВКонтакте", "")

    celName = find.strip()

    if typeName == 'name':
        # return re.search("^[A-Za-zА-Яа-я]*",celName).group(0)
        name = re.search("^.*\s",celName).group(0)
        return name.strip()
    elif typeName == 'surname':
        # return re.search("[A-Za-zА-Яа-я]*$",celName).group(0)
        surname = re.search("\s.*$",celName).group(0)
        return surname.strip()
    else:
        return celName

# print(find[0].get('title'))

# print(re.search("/<title>(.*?)<\/title>/",str(find[0])))
# print(str(find[0]))

friendsNames = []

for i in friends:
    # friendsNames.append(getUserName(i))
    # print(getUserName(i))
    pass

# print(friendsNames)

user = friends[4]

print(getUserName(user))
print(getUserName(user,'name'))
print(getUserName(user,'surname'))
