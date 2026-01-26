passengers = int(input())
capacity = int(input())

count = 0

while capacity > passengers:
    capacity -= passengers
    count += 1

print(count)