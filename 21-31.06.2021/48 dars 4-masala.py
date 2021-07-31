#4.Uchta a, b va c butun son berilgan. Ulardan faqat musbatlari kvadratini
# hisoblab chiquvchi dastur tuzing.
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a<=0:
 a=0
else:
 a=a*a
if b<=0:
 b=0
else:
 b=b*b
if c<=0:
 c=0
else:
 c=c*c
s=a+b+c
print(a,b,c)