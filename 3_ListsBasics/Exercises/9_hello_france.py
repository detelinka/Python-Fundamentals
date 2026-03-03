items = input().split("|")
budget = float(input())

bought_items = []
initial_budget = budget

for element in items:
    item, price = element.split("->")
    price = float(price)

    if item == "Clothes" and price <= 50 and budget >= price:
        budget -= price
        bought_items.append(price)

    elif item == "Shoes" and price <= 35 and budget >= price:
        budget -= price
        bought_items.append(price)

    elif item == "Accessories" and price <= 20.50 and budget >= price:
        budget -= price
        bought_items.append(price)

# Now sell everything
new_prices = []
profit = 0

for price in bought_items:
    new_price = price * 1.4
    new_prices.append(new_price)
    profit += new_price - price
    budget += new_price

# Print results
for p in new_prices:
    print(f"{p:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")