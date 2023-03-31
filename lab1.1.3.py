#  Function to take input from user
def takeInput():
    return int(input("Enter first number: ")), int(input("Enter second number: ")), input("Enter operator (+, -, *, /): ")

# Function to calculate and display result
def displayResult(num1, num2, op):
    result = None
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid operator entered.")
        return
    print(f"{num1} {op} {num2} = {result}")

# Calling the functions to get user input and display result
num1, num2, op = takeInput()
displayResult(num1, num2, op)
