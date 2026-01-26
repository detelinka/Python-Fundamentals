word_1 = input()
word_2 = input()

for char in range(len(word_1)):
    left = word_2[:char + 1]
    right = word_1[char + 1:]
    new = left + right

    if word_1[char] != word_2[char]: print(new)