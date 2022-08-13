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


def is_resource_sufficient(drink_name: object) -> object:
    """ Returns True if the ingredients are enough to make the drink. If not, returns False"""
    for item in drink_name:
        if drink_name[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """ Calculate the total amount inserted by the vendor """
    print(f"Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_money_sufficient(given, spent):
    """ Returns True if the given money is enough to order the drink. If not, returns False"""
    if spent > given:
        print(f"Sorry that's not enough money. Money refunded. ")
        return False
    return True


def is_transaction_success(cost):
    """ Returns profit based on the drink ordered"""
    global profit
    profit += cost
    return profit

def make_coffee(choice, drink_name):
    """ Print the drink name with enjoy message"""
    for item in drink_name:
        resources[item] -= drink_name[item]
    print(f"Here is your {choice} Enjoy!.")

profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()


    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]["ingredients"]
        result = is_resource_sufficient(drink)
        if result:
            given_amount = process_coins()
            print(f"given_amount: {given_amount}")
            enough_money = is_money_sufficient(given_amount, MENU[choice]["cost"])
            print(f"enough_money: {enough_money}")
            if enough_money:
                print(f"Here is ${round(given_amount - MENU[choice]['cost'], 2)} dollars in change.")
                profit = is_transaction_success(MENU[choice]["cost"])
                print(f"profit: {profit}")
                make_coffee(choice, drink)


