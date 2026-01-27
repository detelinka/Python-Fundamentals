n = int(input())

for a in range(ord('a'), ord('a') + n):
    for b in range(ord('a'), ord('a') + n):
        for c in range(ord('a'), ord('a') + n):
            print(chr(a) + chr(b) + chr(c))