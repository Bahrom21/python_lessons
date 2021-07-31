import math
a=int(input("a="))
x=int(input("x="))
y=int(input("y="))

G=(math.cos(2*abs(y+x)-(x+y))**(4*x*x))/(math.atan(x+a)**4*x**5)
print(G)