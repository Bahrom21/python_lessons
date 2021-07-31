"""# amaliy mashg'ulot. 2-masala
#butun sonlardan iborat ruyxat berilgan.juftlarini ekranga chiqarish.
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
for son in sonlar:
    if son % 2 ==0:
        print(sonlar)
#3-masala. butun sonlardan iborat ruyxat berilgan. oldin juftlarini keyin toqlarini yangi ruyxatga
# o'zlashtirib konsulga chiqaring.

sonlar = [2, 9, 6, 4, 5, 3, 7, 8]
sonlar1 = []
for son in sonlar:
    if son % 2 ==0:
        sonlar1.append(son)
for son in sonlar:
    if son % 2 == 1:
        sonlar1.append(son)
print(sonlar1)

#4-masala. toq elementlarining kv.lariga juft elementlarining ikkilanganiga
# almashtirilsin.
"""
"""
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]

for son in sonlar:
    if son % 2 == 0:
        print(sonlar.index(son))
        sonlar[sonlar.index(son)] = son * 2
    else:
        print(sonlar.index(son))
        sonlar[sonlar.index(son)] = son ** 2
"""
#5-masala
indeks = int(input("=>"))
a = []
for i in range(indeks + 1):
    if i == 0 or i == 1:
        a.append(1)
    else:
        a.append(a[i - 1] + a[i - 2])

print(a)
