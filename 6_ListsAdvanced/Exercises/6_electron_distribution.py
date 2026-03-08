electrons = int(input())

shells = []
n = 1  # shell position, starting from 1

while electrons > 0:
    capacity = 2 * (n ** 2)
    to_put = min(capacity, electrons)
    shells.append(to_put)
    electrons -= to_put
    n += 1

print(shells)
