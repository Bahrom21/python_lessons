# 4-masala.06.07.
a = (1, 2, 3, 4, 5, 6)
juft = []
toq = []

for i in range(len(a)):
    if (i + 1) % 2 == 0:
        juft.append(a[i])
    else:
        toq.append(a[i])
print(juft)
print(toq)
