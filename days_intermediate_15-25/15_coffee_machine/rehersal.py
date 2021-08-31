from menu import MENU, resources


def are_resources_sufficient(order_resources, machine_resources):
    for item in order_resources["ingredients"]:
        if order_resources["ingredients"][item] > machine_resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total_coins_inserted = int(input("how many quarters?: ")) * 0.25
    total_coins_inserted += int(input("how many dimes?: ")) * 0.1
    total_coins_inserted += int(input("how many nickles?: ")) * 0.05
    total_coins_inserted += int(input("how many pennies?: ")) * 0.01
    return total_coins_inserted


def is_transaction_successful(money_inserted, drink):
    global profit
    if money_inserted < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if money_inserted > MENU[drink]["cost"]:
            print(f"Here is ${round((money_inserted - MENU[drink]['cost']),2)} dollars in change.")
        profit += MENU[drink]["cost"]
        return True


def make_coffee(order_resources, machine_resources, choice):
    for item in order_resources["ingredients"]:
        machine_resources[item] -= order_resources['ingredients'][item]
    print(f"Here is your {choice} ☕️. Enjoy!”")


profit = 0
coffee_machine_on = True
while coffee_machine_on:
    choices = ["espresso", "latte", "cappuccino"]
    client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if client_choice == "off":
        coffee_machine_on = False
    elif client_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif client_choice in choices:
        if are_resources_sufficient(MENU[client_choice], resources):
            total_coins = process_coins()
            if is_transaction_successful(total_coins, client_choice):
                make_coffee(MENU[client_choice], resources, client_choice)
    else:
        print("Sorry, we don't have that. Choose again.")
