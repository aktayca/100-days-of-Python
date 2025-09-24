from art import coffee, logo, coffee_logo

MENU = {
    "espresso": {
        "ingredients": {
            "Water💧": 50,
            "Coffee☕": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water💧": 200,
            "Coffee☕": 24,
            "Milk🥛": 150
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water💧": 250,
            "Coffee☕": 24,
            "Milk🥛": 100,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water💧": 300,
    "Milk🥛": 200,
    "Coffee☕": 100,
    "Money💵": 0,
}
def check_ingredients(drink):
    if drink in MENU:
        if resources["Water💧"] >= MENU[drink]["ingredients"]["Water💧"]:
            if resources["Coffee☕"] >= MENU[drink]["ingredients"]["Coffee☕"]:
                try:
                    if resources["Milk🥛"] >= MENU[drink]["ingredients"]["Milk🥛"]:
                        return True
                    else:
                        print("Sorry, there is not enough milk in the machine.")
                        return
                except KeyError:
                    return True
            else:
                print("Sorry, there is not enough coffee in the machine.")
                return
        else:
            print("Sorry, there is not enough water in the machine.")
            return
    else:
        return
def coin_input(drink):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    quarters_value = 0.25 * quarters
    dimes_value = 0.10 * dimes
    nickels_value = 0.05 * nickels
    pennies_value =0.01 * pennies
    total_value = pennies_value + nickels_value + dimes_value + quarters_value

    if total_value > MENU[drink]["cost"]:
        print(f"Here is ${round(total_value - MENU[drink]['cost'], 2)} change💵. Enjoy your {drink}☕!")
        return True
    elif total_value == MENU[drink]["cost"]:
        print(f"Enjoy your {drink}!☕")
        return True
    else:
        print(f"Sorry that's not enough money. You gave ${total_value}. {drink.title()} costs ${MENU[drink]['cost']}. Money refunded.")

def update_resources(drink):
    resources["Water💧"] -= MENU[drink]["ingredients"]["Water💧"]
    resources["Coffee☕"] -= MENU[drink]["ingredients"]["Coffee☕"]
    resources["Money💵"] += MENU[drink]["cost"]
    try:
        resources["Milk🥛"] -= MENU[drink]["ingredients"]["Milk🥛"]
    except KeyError:
        return


order = "yes"
while order != "off":
    print(coffee_logo)
    order = input("☕What would you like? Espresso, Latte or Cappuccino?☕ \n").lower()
    if order == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")

    if check_ingredients(order) == True:
        if coin_input(order) == True:
            update_resources(order)
quit()
