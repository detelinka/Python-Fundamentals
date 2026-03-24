force_sides = {}          # side -> list of users
user_to_side = {}         # user -> side

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        force_side, force_user = line.split(" | ")

        if force_user not in user_to_side:
            # ensure side exists
            if force_side not in force_sides:
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)
            user_to_side[force_user] = force_side

    else:  # "{force_user} -> {force_side}"
        force_user, force_side = line.split(" -> ")

        # if user exists, remove from old side
        if force_user in user_to_side:
            old_side = user_to_side[force_user]
            force_sides[old_side].remove(force_user)

        if force_side not in force_sides:
            force_sides[force_side] = []

        force_sides[force_side].append(force_user)
        user_to_side[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")

for side, users in force_sides.items():
    if users:   # only sides with members
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
