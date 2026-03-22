stock = {}

while True:
    line = input()

    if line == "statistics":
        break

    products, quantity = line.split(": ")
    if products in stock: stock[products] += int(quantity)
    else: stock[products] = int(quantity)

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")