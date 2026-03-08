def chars_in_range(start_char, end_char):
    start = ord(start_char)
    end = ord(end_char)

    result_chars = []
    for code in range(start + 1, end):
        result_chars.append(chr(code))

    return " ".join(result_chars)

first = input()
second = input()
print(chars_in_range(first, second))