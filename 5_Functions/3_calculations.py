operator = input()
num1 = int(input())
num2 = int(input())

def calculate(operator, num1, num2):
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    elif operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 // num2

print(calculate(operator, num1, num2))