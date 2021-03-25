fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:        #fruit yra kreipinys į vieną elementas iš listo
    print(fruit)
    print(fruit + " Pie")

for number in range (1, 10, 5):    #neįskaitant 10, žingnis kas 5
    print(number)


total = 0
for number in range(1, 101):
    total += number
print(total)