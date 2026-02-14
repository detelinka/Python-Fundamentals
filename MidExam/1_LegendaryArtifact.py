energy = float(input())
energy = round(energy, 2)

mountain = 0
artifacts = 0

while True:
    terrain = input()

    if terrain == "Journey ends here!":
        break

    if terrain == "mountain":
        energy -= 10
        mountain += 1

        if mountain % 3 == 0:
            artifacts += 1

    elif terrain == "desert":
        energy -= 15

    elif terrain == "forest":
        energy += 7

    if artifacts == 3:
        print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
        exit()

    if energy <= 0:
        print("The character is too exhausted to carry on with the journey.")
        exit()

print(f"The character could not find all the pieces and needs {3 - artifacts} more to complete the legendary artifact.")