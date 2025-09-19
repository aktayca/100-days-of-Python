from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

while True:
    operation = {}
    loop = "Yes"
    print(logo)
    n1 = int(input("First Number: \n"))
    operations = input("Which operation? '+', '-', '/', '*' \n")
    n2 = int(input("Second Number: \n"))


    while loop.title() == "Yes":

        operation["+"] = add(n1, n2)
        operation["-"] = sub(n1, n2)
        operation["*"] = mult(n1, n2)
        operation["/"] = div(n1, n2)

        def calculate():
            return operation[operations]

        print(f"The result of your calculation is: {calculate()}.")
        loop = input("Do you want to continue calculation with the result?\nType 'Yes' if you do.")
        if loop == "Yes":
            n1 = calculate()
            operations = input("Which operation? '+', '-', '/', '*' \n")
            n2 = int(input("Second Number: "))
            calculate()
        else:
            print("\n" * 25)
            break