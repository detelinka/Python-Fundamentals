passengers = int(input())
capacity = int(input())

count = 0

while passengers > 0:
    passengers -= capacity
    count += 1

print(count)