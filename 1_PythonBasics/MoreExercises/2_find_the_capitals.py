text = input()

indices = []

for i in range(len(text)):
    if text[i].isupper():
        indices.append(i)

print(indices)
