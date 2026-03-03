string = input().split()
n = int(input())

for _ in range(n):
    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]
    deck = []

    for i in range(len(left)):
        deck.append(left[i])
        deck.append(right[i])
    string = deck.copy()

print(deck)