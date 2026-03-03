events = input().split("|")

energy = 100
coins = 100
bakery_is_open = True

for event in events:
    values = event.split("-")
    type, value = values[0], int(values[1])

    if type == "rest":
        initial_energy = energy
        energy += value

        if energy > 100:
            energy = 100
        gained = energy - initial_energy

        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')

    elif type == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins < value:
            print(f"Closed! Cannot afford {type}.")
            bakery_is_open = False
            break
        else:
            print(f"You bought {type}.")
            coins -= value

if bakery_is_open == True:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")