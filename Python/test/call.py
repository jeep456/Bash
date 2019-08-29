import time
import subprocess

currentTime = time.strftime("%d-%m-%Y %H:%M:%S")

print(currentTime)

# subprocess.call(['transmission-gtk'])
# subprocess.call(['/usr/bin/transmission-gtk'])

# subprocess.run(['transmission-gtk'])
# subprocess.run(['/usr/sbin/transmission-gtk'])
subprocess.call(['/usr/bin/transmission-gtk'])
# subprocess.call(['transmission-gtk'])
# subprocess.run(['transmission-gtk'])
# subprocess.call(['transmission-gtk'])