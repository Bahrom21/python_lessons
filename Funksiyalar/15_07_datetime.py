"""
vaqt=dt.datetime.now()

print(vaqt.year)
print(vaqt.month)
print(vaqt.day)
print(vaqt.hour)
print(vaqt.minute)
print(vaqt.second)
def vaqt(t)
    print(f"soat:{t.hour}:{t.minute} bo`ldi")
vaqt(t)
"""
"""
x=dt.datetime(2021, 7, 15)
print(dt)"""
"""
import datetime

x = datetime.datetime(2021,7,15)
print(x)
"""
"""
import datetime as dt
x=dt.datetime.now().second:
print(x)
print(x.strftime("%B"))
"""

import datetime as dt
x = dt.datetime.now().second
while True:
    print(dt.datetime.now().second - x)
    if x + 5 == dt.datetime.now().second:
        print("salom")
        x = dt.datetime.now().second
        break