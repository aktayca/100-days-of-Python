from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import coffee_logo

coffee_menu = Menu()
zeynep = CoffeeMaker()
ilker = MoneyMachine()

order = "yes"
print(coffee_logo)
while order != "off":
    order = input(f"Hello! What can I get you today? We have {coffee_menu.get_items()} \n").lower()
    if order == "report":
        zeynep.report()
        ilker.report()
        continue
    elif order == "off":
        quit()
    drink = coffee_menu.find_drink(order)
    if zeynep.is_resource_sufficient(drink) == True:
        if ilker.make_payment(drink.cost) == True:
            zeynep.make_coffee(drink)