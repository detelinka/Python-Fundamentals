while True:
    number = float(input())

    if number < 1 or number > 100: continue

    if 1 <= number <= 100: print(f'The number {number} is between 1 and 100')
    break