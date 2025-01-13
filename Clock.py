from datetime import datetime
import time

c=datetime.now()
h=c.hour
m=c.minute
s=c.second
while True:
    print(f'{h:02d}:{m:02d}:{s:02d}')
    s+=1
    if s==60:
        s=0
        m+=1
    if m==60:
        m=0
    if h==24:
        h=0
    time.sleep(1)
    