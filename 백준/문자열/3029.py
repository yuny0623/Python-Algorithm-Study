# 1029 
from datetime import datetime

now = input()
throw = input()

hour = 0
min = 0
sec = 0
if int(now[:2]) > int(throw[:2]):
    hour = (24 - int(now[:2])) + int(throw[:2])
else:
    hour = int(throw[:2]) - int(now[:2])

if int(now[3:5]) > int(throw[3:5]):
    min = (60 - int(now[3:5])) + int(throw[3:5])
    if min >= 60:
        hour += 1
        if hour >= 24:
            hour = 0
        min = 60 - min

if int(now[6:8]) > int(throw[6:8]):
    sec = (60 - int(now[6:8])) + int(throw[6:8])
    if sec >= 60:
        min += 1
        if min >= 60:
            min = 0
            hour += 1
            if hour >=24:
                hour = 0
        sec = 60 - sec

print(str(hour)+":"+str(min)+":"+str(sec))