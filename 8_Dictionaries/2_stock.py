stock = input().split()
inventory = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    value = int(stock[i + 1])
    inventory[key] = int(value)

products = input().split()
for product in products:
    if product in inventory:
        print(f"We have {inventory[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")