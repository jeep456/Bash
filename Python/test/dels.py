import subprocess
import delegator

s = subprocess

# s.call(["echo","{1..5}"])

d = delegator

d.run('ls')
