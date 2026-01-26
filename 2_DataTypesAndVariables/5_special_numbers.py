n = int(input())

for num in range(1, n + 1):
    digit_sum = 0
    digits = num

    while digits > 0:
        digit_sum += digits % 10
        digits //= 10

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")