text = input()
chars = {}

for ch in text:
    if ch == " ":
        continue
    chars[ch] = chars.get(ch, 0) + 1

for ch, count in chars.items():
    print(f"{ch} -> {count}")
