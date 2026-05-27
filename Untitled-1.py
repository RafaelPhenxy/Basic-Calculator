input("Press any key to continue for the calculator")

numb1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *(multiplication),/(division)): ")
numb2 = float(input("Enter the second number: "))


if operation == "+":
    result = numb1 + numb2

elif operation == "-":
    result = numb1 - numb2

elif operation == "*":
    result = numb1 * numb2

elif operation == "/":
    if numb2 != 0:
        result = numb1 / numb2
    elif numb2 == 0:
        print("Error")

else:
    print("Invalid operation")


print("Result: ", result)