import sys
import pydoc
import os
from subprocess import call

file = "modules.txt"

def output_help_to_file(filepath, request):
    f = open(filepath, 'w')
    sys.stdout = f
    pydoc.help(request)
    f.close()
    sys.stdout = sys.__stdout__
    return

if os.path.exists(file):
    os.remove(file)
    call(['notify-send','-i','software-update-urgent','Файл удалён'])
else:
    output_help_to_file(file,'modules')
    call(['notify-send', '-i', 'emblem-default', 'Файл \'modules\' создан'])