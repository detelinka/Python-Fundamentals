parts = input().split()
total = 0

for s in parts:
    first = s[0]
    last = s[-1]
    num = int(s[1:-1])

    # position in alphabet: A/a -> 1, B/b -> 2, ...
    first_pos = ord(first.lower()) - ord('a') + 1
    last_pos = ord(last.lower()) - ord('a') + 1

    if first.isupper():
        num /= first_pos
    else:
        num *= first_pos

    if last.isupper():
        num -= last_pos
    else:
        num += last_pos

    total += num

print(f"{total:.2f}")
