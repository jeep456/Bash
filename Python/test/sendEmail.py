import smtplib


server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
# server.connect()
# server.startssl()
# server.ehlo()
server.login("jeep456", "predator44")
# message = "\r\n".join([
#         "jeep456@yandex.ru",
#         "dmitriisinov@mail.ru",
#         "Subject: тема",
#         "",
#         str("Hekki")
#     ])
server.sendmail("jeep456@yandex.ru","dmitriisinov@mail.ru","message")
# server.quit()

def sendEMail(text):
    server = smtplib.SMTP("smtp.yandex.ru", 465)
    server.ehlo()
    server.starttls()
    server.login("jeep456", "predator44")
    message = "\r\n".join([
        "jeep456@yandex.ru",
        "To: кому",
        "Subject: тема",
        "",
        str(text)
    ])
    server.sendmail("jeep456@yandex.ru", "dmitriisinov@mail.ru", message)
    # server.quit()

sendEMail('Hello Jeeno')









# import smtplib
#
# HOST = "smtp.yandex.ru"
# SUBJECT = "Test email from Python"
# TO = "dmitriisinove@mail.ru"
# FROM = "jeep456@yandex.ru"
# text = "Python 3.4 rules them all!"
#
# BODY = "\r\n".join((
#     "From: %s" % FROM,
#     "To: %s" % TO,
#     "Subject: %s" % SUBJECT,
#     "",
#     text
# ))
#
# server = smtplib.SMTP(HOST, 465)
# server.sendmail(FROM, [TO], BODY)
# server.quit()
