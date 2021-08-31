print("Python pizza at your service :)")
pizza_size = input("What size of pizza would you like to order? S, M or L: ")
add_pepperoni = input("Would you like to add pepperoni? Say Y or N ")
extra_cheese = input("Would you like to add cheese? Say Y or N ")
bill = 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f'Your final bill is: ${bill}')