n = int(input())
word = input()
strings = []

for _ in range(n):
    n = input()
    strings.append(n)

print(strings)

for i in range(len(strings) - 1, -1, -1):
    string = strings[i]

    if word not in string:
        strings.remove(string)

print(strings)