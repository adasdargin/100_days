print("Welcome to rollercoaster")
height = int(input("Please tell me your height in cm: "))
bill = 0

if height >= 120:
    print("You may ride")
    age = int(input("Please tell me your age: "))
    if age < 12:
        bill = 5
        print(f'Your price is {bill}')
    elif age <= 18:
        bill = 7
        print(f'Your price is {bill}')
    elif age >= 45 and age < 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print(f'Your price is {bill}')
    photo = input("Do you want a photo? Y or N: ")
    if photo == "Y":
        bill += 3
    print(f'Your final bill is: ${bill}')
else:
    print("I'm sorry, you can't ride")