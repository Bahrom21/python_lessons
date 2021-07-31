# 2 - masala
n = int(input("n = "))


def buluvchilar(a):
    for i in range(1, a + 1):
        if a % i == 0:
            print(i, end=" ") # print(i, end="\n") == print(i)


buluvchilar(n)