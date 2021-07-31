#3.Bir birlik uzunlik ‘-’ ga teng. Berilgan n
#uzunlikdagi ‘-’ belgidan iborat chiziq chizuvchi
#dastur tuzing. Protseduradan foydalaning.
"""
print('nechta _ belgisi qo`yilsin? a=')
a=int(input())
print('_'*a)
"""

# 3 - masala
n = int(input("n = "))


def nYulduz(n):
    for i in range(n):
        print(n * "*")