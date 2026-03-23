resource_quantities = {}

while True:
    resource = input()
    if resource == "stop":
        break

    quantity = int(input())

    if resource not in resource_quantities:
        resource_quantities[resource] = 0
    resource_quantities[resource] += quantity

for resource, quantity in resource_quantities.items():
    print(f"{resource} -> {quantity}")
