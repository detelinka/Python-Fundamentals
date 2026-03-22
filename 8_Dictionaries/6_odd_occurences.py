words = input().lower().split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

result = []
for word in words:
    if counts[word] % 2 == 1 and word not in result:
        result.append(word)

print(" ".join(result))