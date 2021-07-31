# yaratish
# f = open("men_haqimda.txt", "x")

# isminni yozaman
f = open("men_haqimda.txt", 'w')
f.write("Oybek")

# konsolga chiqarish
f = open("men_haqimda.txt", 'r')
print(f.read())

# familiyamni yozaman
f = open("men_haqimda.txt", "a")
f.write("Narzullayev")

# konsolga chiqarish
f = open("men_haqimda.txt", 'r')
print(f.read())