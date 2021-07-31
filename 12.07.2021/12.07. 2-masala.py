# 56-dars 1-misol
#n va k butun musbat sonlar berilgan. n va k qatnashgan ushbu ifodani hisoblang.
#n!/k!(n-k)! Funksiyadan foydalaning.

def factorial(n):
 if n==0:
 return 1
 else:
 natija=n*factorial(n-1)
 return natija
n=int(input('n= '))
k=int(input('k= '))
m=n-k
N=factorial(n)
K=factorial(k)
M=factorial(m)
S=N/(K*M)
print('natija=',S)
