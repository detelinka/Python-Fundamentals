def odd_even_sum(some_number: str) -> str:

    sum_odd = 0
    sum_even = 0

    for i in some_number:
        if int(i) % 2 == 0: sum_even += int(i)
        else: sum_odd += int(i)

    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

number = input()
print(odd_even_sum(number))