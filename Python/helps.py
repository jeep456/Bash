import time

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def today():
    return time.strftime("%Y-%m-%d")

def timeNow():
    return time.strftime("%H:%M:%S")

def getTimeFormat(format):
    if format == 'H':
        return time.strftime("%H")
    elif format == 'M':
        return time.strftime("%M")
    elif format == 'S':
        return time.strftime("%S")

# print(Carbon().now())

# print(int(getTimeFormat('M')))