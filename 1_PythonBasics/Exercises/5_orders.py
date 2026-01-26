n = int(input())
total_price = 0

for _ in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if not (0.01 <= price <= 100.00):
        continue
    if not (1 <= days <= 31):
        continue
    if not (1 <= capsules <= 2000):
        continue

    order_price = price * days * capsules
    total_price += order_price

    print(f'The price for the coffee is: ${order_price:.2f}')


print(f'Total: ${total_price:.2f}')