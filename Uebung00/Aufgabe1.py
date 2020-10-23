def simple_calc(firstNumber: float, operator: str, secondNumber: float):
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


simple_calc(
    float(input("Enter your first Number: ")),
    input("Enter your Operator(+,-,/,*): "),
    float(input("Enter your second Number: ")),
)
