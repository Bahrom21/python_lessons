# 1-masala. 01.08.2021
# 1 dan 10 gacha bo'lgan sonlarni

import random
while True:
    tasodifiySon =random.randint(1, 10)
    kiritilganSon = int(input("son-"))
    if kiritilganSon == tasodifiySon:
        print(tasodifiySon)
        print("yutdingiz")
        break
    else:
        print(tasodifiySon)
        print("dam oling")
