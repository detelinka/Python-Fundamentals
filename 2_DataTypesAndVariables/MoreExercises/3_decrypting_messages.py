key = int(input())
n = int(input())

final = ''

for _ in range(n):
    ch = input()
    final += chr(ord(ch) + key)

print(final)
