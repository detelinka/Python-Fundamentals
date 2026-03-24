products = {}

while True:
    line = input()
    if line == "buy":
        break

    name, price, qty = line.split()
    price = float(price)
    qty = int(qty)

    if name not in products:
        products[name] = {"price": price, "qty": qty}
    else:
        products[name]["qty"] += qty
        products[name]["price"] = price

for name, data in products.items():
    total_price = data["price"] * data["qty"]
    print(f"{name} -> {total_price:.2f}")