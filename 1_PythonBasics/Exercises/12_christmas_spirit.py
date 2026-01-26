decorations = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

ornament_price = 2
skirt_price = 5
garland_price = 3
lights_price = 15

for day in range(1, days + 1):

    if day % 11 == 0:
        decorations += 2
    if day % 2 == 0:
        total_cost += ornament_price * decorations
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (skirt_price + garland_price) * decorations
        total_spirit += 3 + 10
    if day % 5 == 0:
        total_cost += lights_price * decorations
        total_spirit += 17
        if day % 3 == 0: total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += skirt_price + garland_price + lights_price

if days % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')