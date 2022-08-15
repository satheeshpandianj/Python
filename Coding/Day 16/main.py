from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    all_items = menu.get_items()
    choice = input(f"what would you to like to drink? {all_items}:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money.report()
        coffee.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
                money.report()


