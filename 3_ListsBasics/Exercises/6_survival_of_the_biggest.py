integers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    integers.remove(min(integers))

print(*integers, sep=', ')