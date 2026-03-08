numbers = [int(number) for number in input().split(", ")]
group = 10
while numbers:
    current_group = [n for n in numbers if n <= group]
    print(f"Group of {group}'s: {current_group}")

    # remove taken numbers from the original list
    numbers = [n for n in numbers if n > group]
    group += 10