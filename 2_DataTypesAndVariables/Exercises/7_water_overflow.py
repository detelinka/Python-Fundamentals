n = int(input())
capacity = 255

for _ in range(n):
    liters = int(input())
    if capacity < liters:
        print("Insufficient capacity!")
    else:
        capacity -= liters

print(255 - capacity)