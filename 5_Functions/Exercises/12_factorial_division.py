num1 = int(input())
num2 = int(input())

def factorial(num: int):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

factorial_division = factorial(num1) / factorial(num2)
print(f"{factorial_division:.2f}")