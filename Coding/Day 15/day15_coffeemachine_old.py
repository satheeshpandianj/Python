from data import MENU, resources

print(MENU[f"latte"]["cost"])
# TODO 2: Print report, When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

MONEY = 0
WATER_QTY = resources["water"]
MILK_QTY = resources["milk"]
COFFEE_QTY = resources["coffee"]

def print_report(resources):
    print(f"Water : {WATER_QTY}")
    print(f"Milk : {MILK_QTY}")
    print(f"Coffee : {COFFEE_QTY}")
    print(f"Money : ${MONEY}")


def check_resources(coffee_type):
    if resources["water"] >= MENU[f"{coffee_type}"]["ingredients"]["water"]:
        if resources["milk"] >= MENU[f"{coffee_type}"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[f"{coffee_type}"]["ingredients"]["coffee"]:
                return 0
            else:
                print(f"There isn't enough coffee to prepare {coffee_type}")
                return 1
        else:
            print(f"There isn't enough milk to prepare {coffee_type}")
            return 1
    else:
        print(f"There isn't enough water to prepare {coffee_type}")
        return 1

def check_resources_espresso(coffee_type):
    if resources["water"] >= MENU[f"{coffee_type}"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[f"{coffee_type}"]["ingredients"]["coffee"]:
            return 0
        else:
            print(f"There isn't enough coffee to prepare {coffee_type}")
            return 1
    else:
        print(f"There isn't enough water to prepare {coffee_type}")
        return 1


def insert_coins():
    print(f"Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickles) * 0.05 + float(pennies) * 0.01
    print(f"Total Given: {total}")
    return total


def calc(given, spent, choice):
    if given > spent:
        print(f"Here is ${round(given - spent,2)} in change")
        print(f"Here is your {choice} Enjoy!")
    else:
        print(f"There isn't enough money to buy {choice}")

def update_resources(WATER_QTY,MILK_QTY,COFFEE_QTY,MONEY):
    WATER_QTY -= MENU[f"{user_choice}"]["ingredients"]["water"]
    MILK_QTY -= MENU[f"{user_choice}"]["ingredients"]["milk"]
    COFFEE_QTY -= MENU[f"{user_choice}"]["ingredients"]["coffee"]
    MONEY += MENU[f"{user_choice}"]["cost"]
    return WATER_QTY, MILK_QTY, COFFEE_QTY, MONEY

def update_resources_espresso(WATER_QTY,COFFEE_QTY,MONEY):
    WATER_QTY -= MENU[f"{user_choice}"]["ingredients"]["water"]
    COFFEE_QTY -= MENU[f"{user_choice}"]["ingredients"]["coffee"]
    MONEY += MENU[f"{user_choice}"]["cost"]
    return 0

is_maintenance_going = False

while not is_maintenance_going:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice == "report":
        print_report(resources)
    elif user_choice == "latte" or user_choice == "cappuccino":
        result = check_resources(user_choice)
        if result == 0:
            given = insert_coins()
            expenses = MENU[f"{user_choice}"]["cost"]
            calc(given, expenses, user_choice)
            update = update_resources(WATER_QTY,MILK_QTY,COFFEE_QTY,MONEY)
        else:
            print(f"Please refill the resources")
    elif user_choice == "espresso":
        result = check_resources_espresso(user_choice)
        if result == 0:
            given = insert_coins()
            expenses = MENU[f"{user_choice}"]["cost"]
            calc(given, expenses, user_choice)
            update = update_resources_espresso(WATER_QTY,COFFEE_QTY,MONEY)
            print(f"Water: {WATER_QTY}")
        else:
            print(f"Please refill the resources")
    elif user_choice == "off":
        is_maintenance_going = True
    else:
        print(f"Wrong input")

