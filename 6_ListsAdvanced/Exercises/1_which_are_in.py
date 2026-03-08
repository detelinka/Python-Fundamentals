first_list = input().split(", ")
second_list = input().split(", ")

substring = []

for string_1 in first_list:
    for string_2 in second_list:
        if string_1 in string_2:
            substring.append(string_1)
            break

print(substring)