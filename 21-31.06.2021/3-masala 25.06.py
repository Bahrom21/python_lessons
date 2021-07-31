import math
y=int(input("y="))
h=int(input("h="))

A=(math.tan(y**3-h**4)+h**2)/(math.sin(h)**2+y)
print(A)