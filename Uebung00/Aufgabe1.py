firstNumber = input("Enter your first Number: ")
operator = input("Enter your Operator(+,-,/,*): ")
secondNumber = input("Enter your second Number: ")
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)
if operator == "+":
    print(firstNumber + secondNumber)
elif operator == "-":
    print(firstNumber - secondNumber)
elif operator == "/":
    print(firstNumber / secondNumber)
elif operator == "*":
    print(firstNumber * secondNumber)
else:
    print("Error: Unsupported Operator")