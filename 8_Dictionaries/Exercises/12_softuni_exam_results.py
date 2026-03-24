results = {}       # username -> max points
submissions = {}   # language -> count

while True:
    line = input()
    if line == "exam finished":
        break

    parts = line.split("-")

    if parts[1] == "banned":
        username = parts[0]
        if username in results:
            del results[username]
        # do NOT touch submissions counts
    else:
        username, language, points = parts[0], parts[1], int(parts[2])

        # count every submission, even from users later banned
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        # store max points per user (regardless of language in this task spec)
        if username not in results:
            results[username] = points
        else:
            if points > results[username]:
                results[username] = points

print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
