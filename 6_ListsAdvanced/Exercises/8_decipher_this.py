def decipher_message(text):
    words = text.split()
    result = []

    for word in words:
        # 1. Extract the leading digits (ASCII code)
        num_str = ''
        i = 0
        while i < len(word) and word[i].isdigit():
            num_str += word[i]
            i += 1

        first_char = chr(int(num_str))        # decoded first letter
        rest = list(word[i:])                 # remaining characters as list

        # 2. Swap second and last letters back (if enough length)
        if len(rest) >= 2:
            rest[0], rest[-1] = rest[-1], rest[0]

        decoded_word = first_char + ''.join(rest)
        result.append(decoded_word)

    return ' '.join(result)

secret = input()
print(decipher_message(secret))