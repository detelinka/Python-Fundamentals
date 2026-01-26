budget = float(input())
price_per_kg = float(input())

eggs_price = price_per_kg * 0.75
milk_price = price_per_kg * 1.25
milk_for_one_bread = milk_price * 0.25

bread_cost = price_per_kg + eggs_price + milk_for_one_bread

loaves = 0
colored_eggs = 0

while budget >= bread_cost:
    budget -= bread_cost
    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2


print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')