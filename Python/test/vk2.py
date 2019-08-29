import requests
from bs4 import BeautifulSoup
import json, re

# id = "4582152"
# id = "355177"

userId = "115419543"
token = "941789dfa99e1a399057b7684c1a01be857b757de340049639ca22cbea5974ab69041fcf8f906f803ced4"

message = "Ляпота"

url = "https://api.vk.com/method/messages.send?user_id=" + userId + "&message=" + message + "&v=5.52&access_token=" + token

req = requests.get(url)

print(req)

# friends = json.loads(req)["response"]["items"]

# print(friends)