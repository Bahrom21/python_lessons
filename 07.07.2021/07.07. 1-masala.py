#7.07.2021 1-masala
""" setni yaratish"""
numbers = {1,2,3,4,5,6}
print(type(numbers))

#set() konstruktori bilan
numbers = set([1,2,3,4,5])     #listni setga aylantirish
print(numbers)
print(type(numbers))

numbers = set((1,2,3,4,5))     #listni setga aylantirish
print(numbers)
"""elementlarga ajratish"""
# setda indeks yo'q!!!
# setni listga aylaytirish
numbers = {1,2,3,4,5,6}
numbers = list(numbers)  #numbers listga aylandi
print(type(numbers))


