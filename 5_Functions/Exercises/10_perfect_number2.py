def is_perfect(num: int) -> str:
    divisor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))