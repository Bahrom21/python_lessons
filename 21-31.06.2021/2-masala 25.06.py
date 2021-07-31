#uchburchak 2 tomoni ma'lum. a va b, ular orasidagi burchak berilgan. 3-tomonini toping
import math
a=int(input("a=:"))
b=int(input("b=:"))
x=int(input("x=:"))
x_rad=x/180*math.pi
c=(math.sqrt(a**2+b**2-2*a*b*math.cos(x_rad))
print(c)