num1 = float(input("Please enter the 1st number: "))
op = input("Please enter the operator: ")
num2 = float(input("Please enter the 2nd number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Sorry. Invalid operator. Try again.")
