MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins(drink, drink_price):
    print(f"{drink.capitalize()} price ${drink_price}. Please insert coins:")
    total = int(input("How many quarters $0.25: ")) * 0.25
    total += int(input("How many dimes $0.10: ")) * 0.10
    total += int(input("How many nickles $0.05: ")) * 0.05
    total += int(input("How many pennies $0.01: ")) * 0.01
    return total


def is_transaction_successful(drink_cost, total_coins):
    if drink_cost <= total_coins:
        global profit
        profit += drink_cost
        print(f"Here is your change: ${round(total_coins - drink_cost, 2)}.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(client_choice, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {client_choice}. Enjoy!☕️ ")


coffee_machine_on = True
profit = 0
while coffee_machine_on:
    choice = input("What would you like? ").lower()
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${float(profit)}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            coins = process_coins(choice, drink["cost"])
            if is_transaction_successful(drink["cost"], coins):
                make_coffee(choice, drink["ingredients"])
