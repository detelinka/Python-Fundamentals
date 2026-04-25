animals = {}
areas = {}

while True:
    line = input()
    if line == "EndDay":
        break

    command, data = line.split(": ")
    if command == "Add":
        name, food_str, area = data.split("-")
        food = int(food_str)

        if name not in animals:
            animals[name] = {"food": food, "area": area}
            if area not in areas:
                areas[area] = set()
            areas[area].add(name)
        else:
            animals[name]["food"] += food

    elif command == "Feed":
        name, food_str = data.split("-")
        food = int(food_str)

        if name in animals:
            animals[name]["food"] -= food
            if animals[name]["food"] <= 0:
                area = animals[name]["area"]
                print(f"{name} was successfully fed")
                del animals[name]
                areas[area].discard(name)

print("Animals:")
for name, info in animals.items():
    print(f" {name} -> {info['food']}g")

print("Areas with hungry animals:")
for area, names in areas.items():
    hungry_count = sum(1 for n in names if n in animals)
    if hungry_count > 0:
        print(f" {area}: {hungry_count}")
