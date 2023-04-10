def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def Mul(a , b):
    return a * b

def mod(a, b):
    return a % b

print("Select operation----")
print("1.add")
print("2.sub")
print("3.div")
print("4.Mul")
print("5.mod")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, Please input a number______")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", div(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", Mul(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid input")