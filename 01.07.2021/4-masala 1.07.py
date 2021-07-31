# 4-masala. Sonlar to'plami berilgan Bu sonlarni o'sish tartibida saralang.

sonlar=[1, 5, 9]

for index in range(len(sonlar)):
    for key in range(len(sonlar)):
        if sonlar[index] > sonlar [key]:
           sonlar[index] = sonlar [key] + sonlar[index]
           sonlar[key] = sonlar[index] - sonlar [key]
           sonlar[index] = sonlar[index] - sonlar [key]

sonlar.sort(revers=False)
print(sonlar)