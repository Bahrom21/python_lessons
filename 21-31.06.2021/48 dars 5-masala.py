#48-dars 5-masala. Kvadrat tenglamani yechish dasturini tuzing.
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
D=b*b-4*a*c
from math import*
if D>=0:
 x1=(-b-sqrt(D))/(2*a)
 x2=(-b+sqrt(D))/(2*a)
 print('x1=',x1,'x2=',x2)
else:
 print('yechimga ega emas')
