# a=3, b=4, c=5. Geron formulasi yordamida
import math
a=int(input("a=:"))
b=int(input("b=:"))
c=int(input("c=:"))
p=(a+b+c)/2
S=(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(f"p={p};  S={S}")