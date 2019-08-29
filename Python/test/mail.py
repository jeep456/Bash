import subprocess

theme = "From Python"
to = "jeep456@yandex.ru"
msg = "Привет дядя"

# call(['mail','-s',theme,to,'<<<',msg])
subprocess.check_output(['mail','-s',theme,to,'<<<',msg])