
"""KORTEJLAR (tuple)"""
numbers = (1,2,3,4)

numbers1 = [1,2,3,4]
print(type(numbers))
print(type(numbers1))

#numbers[4]=4 bu xato ish
# qoida. Listda kortejni yangilab bo'lmaydi.

""" KONSTRUKTOR """
a = tuple([1,2,3,4])
print(type(a))

""" kortej elementlariga murojaat"""
numbers = (1,2,3,4)
print(numbers[1])
# bu amallar index lar orqali amalga oshiriladi

#avval kortejni ro'yxatga aylantiramiz
numbers=list(numbers)


""" ---------------------"""
numbers = (1,2,3,4)
i = 0
while i < len(numbers):
    print(numbers[i])
    i+=1

for i in numbers:
    print(i)

#fordan indeks bo'yicha foydalanish
for i in range(len(numbers)):
    print(numbers[i])

""" kortejlarni qo'shish"""
numbers1 = (1,2,3)
numbers2 = (4,5,6)
#qo'shish
numbersall = numbers1+numbers2
print(numbersall)
""" kortejlarni songa ko'paytirish"""
numbers = (1, 2, 3, 4)
numbers = numbers * 2
print(mynumbers)
"""
""" kortej metodlari""" """

numbers = (1,1,2,3,3,4,4,2,2,)
#count()
print(numbers.count(2))