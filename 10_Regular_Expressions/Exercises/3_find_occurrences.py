import re

sentence = input()
word = input()

pattern = rf'\b{re.escape(word)}\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))
