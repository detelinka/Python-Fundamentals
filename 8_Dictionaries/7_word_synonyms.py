n = int(input())
synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonyms in synonyms.items():
    print(f"{word} - {', '.join(synonyms)}")