text = input()

result = []
i = 0

while i < len(text):
    # collect non-digit substring
    substr = ""
    while i < len(text) and not text[i].isdigit():
        substr += text[i]
        i += 1

    # collect following digits as repeat count
    num_str = ""
    while i < len(text) and text[i].isdigit():
        num_str += text[i]
        i += 1

    count = int(num_str)
    result.append(substr.upper() * count)

rage_message = "".join(result)
unique_symbols = len(set(rage_message))

print(f"Unique symbols used: {unique_symbols}")
print(rage_message)
