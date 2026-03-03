fires = input().split("#")
water = int(input())

valid_ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51)
}

put_out_cells = []
effort = 0.0
total_fire = 0

for fire in fires:
    fire_type, value_str = fire.split(" = ")
    value = int(value_str)

    if value not in valid_ranges[fire_type]:
        continue
    if water < value:
        continue

    water -= value
    put_out_cells.append(value)
    total_fire += value
    effort += value * 0.25

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
