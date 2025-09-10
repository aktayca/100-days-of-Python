print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

#Size Prices
if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
elif size.upper() == "L":
    bill += 25

#Extra Pepperoni
if pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    elif size.upper() in ["M", "L"]:
        bill += 3

#Extra Cheese
if cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
