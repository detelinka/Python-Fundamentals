numbers = input().split(".")
n1 = int(numbers[0])
n2 = int(numbers[1])
n3 = int(numbers[2])

n3 += 1
if n3 > 9:
    n3 = 0
    n2 += 1
    if n2 > 9:
        n2 = 0
        n1 += 1

print(f"{n1}.{n2}.{n3}")