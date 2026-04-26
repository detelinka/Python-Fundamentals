animals = input().split(", ")

queue = animals[::-1]

if queue[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    wolf_index = queue.index("wolf")
    print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")
