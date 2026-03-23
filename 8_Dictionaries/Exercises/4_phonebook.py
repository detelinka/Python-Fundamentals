phonebook = {}

# Read "name-number" pairs until we get a line that is just a number (N)
while True:
    line = input()
    if line.isdigit():          # this is N – number of searches
        n = int(line)
        break

    name, number = line.split("-")
    phonebook[name] = number    # add or update entry

# Perform N searches
for _ in range(n):
    name_to_search = input()
    if name_to_search in phonebook:
        print(f"{name_to_search} -> {phonebook[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")
