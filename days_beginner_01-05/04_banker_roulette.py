import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ") #vieną bendrą stringą perkelia į stringų listą išimdamas kablelį ir tarpą
list_length = len(names)

print(names)
print(list_length)

random_name = random.randint(0, list_length - 1)
person_who_will_pay = names[random_name]

#arba
#person_who_will_pay = random.choice(names)
print(f'{person_who_will_pay} is going to buy the meal today!')

#Adas, Evaldas, Jonas, Justas, Arijus, Benas, Herkus, Simas
#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
#https://www.askpython.com/python/string/convert-string-to-list-in-python