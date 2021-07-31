#3-masala. Berilgan sonlar ichidan eng kichigini topish
sonlar=[1, 5, 9, 6, 0, 2, 3]
kichikSon = sonlar[0]
for son in sonlar:
    if kichikSon > son:
        kichikSon=son
print(kichikSon)