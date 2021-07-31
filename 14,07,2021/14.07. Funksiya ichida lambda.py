"""# Funksiya ichida lambda.
def kvadrat(n):
    return lambda a: n == a


son = kvadrat(5)

print(son(2))
print(kvadrat(5n)(2))
"""
"""#masala. 
import math
def aylana(L):
    r=2*math.pi/L
    return lambda s=math.pi*(r**2)
"""
""""
def aylana(l):
    return lambda pi: pi*(l/(2*pi))*2
x=aylana(10)

print(x(3.14))
"""
"""
#def kub(a):     return lambda a: a**2 x=kub(10) print(x)
"""


def ism(n):
    return lambda i: (n + ' ') * i

k = input("ismingizni kiriting: ")
i_ta_ism = ism(k)
print(i_ta_ism(10))
