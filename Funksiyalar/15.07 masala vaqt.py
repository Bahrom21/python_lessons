import datetime as dt
#
# while True:
#     print(datetime.datetime.now())

vaqt = dt.datetime.now()

print(vaqt.year)  # yil
print(vaqt.month)  # oy
print(vaqt.day)  # kun
print(vaqt.weekday())  # hafta kuni 0 dan boshlanadi
print(vaqt.hour)  # soat
print(vaqt.minute)  # minut
print(vaqt.second)  # sekund
print(vaqt.microsecond)  # mikrosekund
t = dt.datetime.now()
def vaqt(t):
    if t.hour<10:
        if t.minute < 10:
            print(f"soat: 0{t.hour}:0{t.minute} bo'ldi")
        else:
            print(f"soat: 0{t.hour}:{t.minute} bo'ldi")
    else:
        if t.minute < 10:
            print(f"soat: {t.hour}:0{t.minute} bo'ldi")
        else:
             print(f"soat: {t.hour}:{t.minute} bo'ldi")
vaqt(t)