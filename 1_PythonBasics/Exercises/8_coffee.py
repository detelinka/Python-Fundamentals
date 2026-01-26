coffees = 0
command = input()

while command != "END":

    if command == 'coding': coffees += 1
    elif command == 'dog': coffees += 1
    elif command == 'cat': coffees += 1
    elif command == 'movie': coffees += 1

    if command == 'CODING': coffees += 2
    elif command == 'DOG': coffees += 2
    elif command == 'CAT': coffees += 2
    elif command == 'MOVIE': coffees += 2

    command = input()

if coffees > 5: print('You need extra sleep')
else: print(coffees)