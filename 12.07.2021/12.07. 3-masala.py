#56-dars 2-masala
#n natural son berilgan. Kvadrati n dan kichik bo‘lgan barcha natural sonlarni chiqaruvchi
#dastur tuzing.

"""from math import*
i=1
n=int(input('n= '))
m=int((sqrt(n)))
while i<=m:
 print(i)
 i+=1"""
"""#1-masala
from math import factorial as f

def myfunction(n, k):
    return f(n) / (f(k) * f(n - k))
print(myfunction(6, 4))"""
#2-masala
n=int(input('n= '))
def myfunction2(n):
    qiymat=[]
    for i in range(1, n):
        if i**2<n:
            qiymat.append(i)
    return qiymat

print(myfunction2(n))