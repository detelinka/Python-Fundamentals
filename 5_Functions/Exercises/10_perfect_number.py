def is_perfect(num: int) -> bool:
    if num <= 1:
        return False

    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num

number = int(input())

if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")