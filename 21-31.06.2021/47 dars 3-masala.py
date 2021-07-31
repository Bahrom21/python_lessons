#47 dars 3-masala. a va b sondan qaysi biri juft ekanligini aniqlovchi dastur tuzing.
a = int(input('a='))
b = int(input('b='))

a1 = a % 10
a2 = b % 10
if a1 % 2 == 0:
    print('a soni juft', a)
else:
    print('a toq son')
if a2 % 2 == 0:
    print('b soni juft', b)
else:
    print('b toq son')
