grid = list(map(int, input().split("|")))
total = 0
size = len(grid)

while True:
    command = input()

    if command == "Adventure over":
        break

    if "Step" in command:
        parts = command.split("$")
        action = parts[0]
        start = int(parts[1])
        steps = int(parts[2])

        if not (0 <= start < size):
            continue

        if "Backward" in action:
            index = (start - steps) % size
        else:
            index = (start + steps) % size

        total += grid[index]
        grid[index] = 0

    elif command.startswith("Double"):
        index = int(command.split()[1])
        if 0 <= index < size:
            grid[index] *= 2

    elif command == "Switch":
        grid.reverse()

print(" - ".join(map(str, grid)))
print(f"Robo finished the adventure with {total} items!")