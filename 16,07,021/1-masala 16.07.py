"""# fayl yaratish
#f=open("mening_faylim.txt", 'x')

#faylni o`qish uchun ochish
#f=open("mening_faylim.txt")   # 'r' -> read
#print(f.read())

#faylni yozish uchun ochish
f = open("mening_faylim.txt", 'w')
f.write("")
#f = open("MenHaqimda.txt",'x')"""

f = open("My_file.txt",'w')
f.write('Bahrom')
f.close()
f= open('Mening_faylim.txt','a')
f.write(' Djumayev')
f.close()
f = open('Mening_faylim.txt','r')
print(f.read())