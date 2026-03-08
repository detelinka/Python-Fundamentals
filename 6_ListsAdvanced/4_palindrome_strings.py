strings = input().split()
print(list(filter(lambda x: x == x[::-1], strings)))

word = input()
count = strings.count(word)
print(f"Found palindrome {count} times")