#47 dars 2 masala
x=int(input('a='))
birlar=x%10      # 215->5
unlar=x%100//10      # 215->15->1
yuzlar=x//100    # 215-> 2

if birlar==unlar or unlar==yuzlar or birlar==yuzlar:
 print('bir hil raqamlar mavjud')
else:
 print('bir hil raqamlar mavjud emas')

