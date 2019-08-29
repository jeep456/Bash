# import telepot, asyncio
#
# tokenBot = 'AAE233AghSpJ9vQyAwrmy77ox7G9-OH6i4Q'
#
# message = 'Hello Darling'
#
# async def get_message(msg):
#
#     global answerData, lowerCountries
#
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     chat_id_str = str(chat_id)
#
#     print('mess')
#
# bot = telepot.Bot(tokenBot)
# bot = telepot.
#
# loop = asyncio.get_event_loop()
#
# loop.create_task(bot.message_loop({'chat':get_message()}))



















#######################################################################################################################
#
# import requests
#
# user = '122066134'
# tokenBot = 'AAE233AghSpJ9vQyAwrmy77ox7G9-OH6i4Q'
# message = 'hello my friend'
#
# url = "https://api.telegram.org/bot566648079:" + tokenBot + "/sendmessage?chat_id=" + user + "&text=" + message
#
# proxy = {
#     'http':'77.242.21.10:8080'
# }
#
# url = 'https://api.telegram.org/bot566648079:AAE233AghSpJ9vQyAwrmy77ox7G9-OH6i4Q/sendmessage?chat_id=381581718&text=hello'
#
# print(requests.get(url,proxies=proxy))
