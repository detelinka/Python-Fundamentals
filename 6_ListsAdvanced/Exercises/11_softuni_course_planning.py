def move_ex(schedule, lesson):
    ex = f"{lesson}-Exercise"
    if ex in schedule:
        schedule.remove(ex)
        i = schedule.index(lesson)
        schedule.insert(i + 1, ex)

schedule = input().split(", ")

while True:
    line = input()
    if line == "course start":
        break

    parts = line.split(":")
    cmd = parts[0]
    lesson = parts[1]

    if cmd == "Add":
        if lesson not in schedule:
            schedule.append(lesson)

    elif cmd == "Insert":
        idx = int(parts[2])
        if lesson not in schedule:
            schedule.insert(idx, lesson)

    elif cmd == "Remove":
        ex = f"{lesson}-Exercise"
        if lesson in schedule:
            schedule.remove(lesson)
        if ex in schedule:
            schedule.remove(ex)

    elif cmd == "Swap":
        other = parts[2]
        if lesson in schedule and other in schedule:
            i1, i2 = schedule.index(lesson), schedule.index(other)
            schedule[i1], schedule[i2] = schedule[i2], schedule[i1]
            move_ex(schedule, lesson)
            move_ex(schedule, other)

    elif cmd == "Exercise":
        ex = f"{lesson}-Exercise"
        if lesson in schedule:
            if ex not in schedule:
                i = schedule.index(lesson)
                schedule.insert(i + 1, ex)
        else:
            schedule.append(lesson)
            schedule.append(ex)

i = 1
for item in schedule:
    print(f"{i}.{item}")
    i += 1