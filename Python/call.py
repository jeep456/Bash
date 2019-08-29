from subprocess import call

vars = 1

if vars == 1:
    # call(['notify-send', '-i', 'emblem-default', "Всё отлично"])
    call(['notify-send', '-i', '/home/jeem/Загрузки/image (1).jpg', "Всё отлично"])
else:
    call(['notify-send', '-i', 'software-update-urgent', "Кошмар конечно"])