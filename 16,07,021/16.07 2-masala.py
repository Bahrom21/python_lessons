f = open("My_file.txt",'w')
f.write('Bahrom')
f.close()

f= open('My_file.txt','a')
f.write(' Djumayev')
f.close()

f = open('My_file.txt','r')
print(f.read())
