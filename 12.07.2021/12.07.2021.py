"""
def fun(num):
    yig = 0
    for i in str(num):
        yig+=int(i)
    print(yig)
fun(n)
Oʏʙᴇᴋ Nᴀʀᴢᴜʟʟᴀʏᴇᴠ, [12.07.21 11:47]
[Переслано от Oʏʙᴇᴋ Nᴀʀᴢᴜʟʟᴀʏᴇᴠ]
# 4 - masala.
n = int(input("n = "))
"""

# def xona_yigindi(a):
#     yigindi = 0
#     for i in range(len(str(a))):
#         yigindi += a // (10 ** i) % 10
#
#     print(yigindi)

def xona_yigindi(a):
    summa = 0
    a = str(a)
    for i in a:
        summa += int(i)
print(summa)

xona_yigindi(n)