n = int(input())

total_free_chairs = 0
enough_chairs_everywhere = True  # flag to track if all rooms are OK

for room in range(1, n + 1):
    data = input().split()
    chairs_str = data[0]          # e.g. "XXXXX"
    visitors = int(data[1])       # e.g. 4

    chairs_count = len(chairs_str)

    if chairs_count < visitors:
        needed = visitors - chairs_count
        print(f"{needed} more chairs needed in room {room}")
        enough_chairs_everywhere = False
    else:
        total_free_chairs += chairs_count - visitors

if enough_chairs_everywhere:
    print(f"Game On, {total_free_chairs} free chairs left")
