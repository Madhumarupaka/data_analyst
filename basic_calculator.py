def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return "ERROR!"
    else:
        return x / y


print("choose operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
while True:
    choice = input("enter the choice(1/2/3/4):")
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("enter the first number:"))
            num2 = float(input("enter the second number:"))
        except ValueError:
            print("Invalid input,enter the valid input")
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", mul(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", div(num1, num2))
        next1 = input("Let's do the next calculation:(Yes/No)")
        if next1 == "No":
            break



    else:
        print("Invalid input")