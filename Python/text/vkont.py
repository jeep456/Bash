import vk_api

vk_session = vk_api.VkApi('termik-2008@mail.ru', 'konstruktivizm44')
vk_session.auth()

vk = vk_session.get_api()

# vk.wall.post(message="Я вас всех обожаю")
frineds = vk.friends.get()

print(frineds)

frineds = tuple("https://vk.com/id" + str(i) for i in frineds['items'])

print(frineds)



# print(search)
# print(search)
