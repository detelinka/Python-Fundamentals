data = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    parts = command.split()
    action = parts[0]

    if action == "merge":
        start = int(parts[1])
        end = int(parts[2])

        # Clamp indices to valid range
        start = max(0, start)
        end = min(len(data) - 1, end)

        if start <= end:
            merged = "".join(data[start:end + 1])
            data[start:end + 1] = [merged]

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        if partitions <= 0:
            continue  # nothing to do, avoid division by zero

        element = data[index]
        part_len = len(element) // partitions
        remainder = len(element) % partitions

        new_parts = []
        start = 0

        # First (partitions - 1) parts with equal length
        for _ in range(partitions - 1):
            new_parts.append(element[start:start + part_len])
            start += part_len

        # Last part gets the remainder (may be longer)
        new_parts.append(element[start:])

        data[index:index + 1] = new_parts

print(" ".join(data))