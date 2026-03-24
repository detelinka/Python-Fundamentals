text = input()

result = []
strength = 0

for i in range(len(text)):
    ch = text[i]

    if ch == ">":
        result.append(ch)
        strength += int(text[i + 1])  # there is always a digit after '>'
    else:
        if strength > 0:
            strength -= 1   # "explode" this character -> skip it
        else:
            result.append(ch)

print("".join(result))
