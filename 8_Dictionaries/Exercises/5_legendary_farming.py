key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}              # preserve order of appearance in Python 3.7+
legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

obtained = None

while not obtained:
    tokens = input().split()
    for i in range(0, len(tokens), 2):
        qty = int(tokens[i])
        material = tokens[i + 1].lower()

        if material in key_materials:
            key_materials[material] += qty
            if key_materials[material] >= 250 and not obtained:
                obtained = legendary_items[material]
                key_materials[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += qty

print(f"{obtained} obtained!")
print(f"shards: {key_materials['shards']}")
print(f"fragments: {key_materials['fragments']}")
print(f"motes: {key_materials['motes']}")

for material, qty in junk.items():
    print(f"{material}: {qty}")
