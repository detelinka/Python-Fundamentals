playlist = input().split()
commands_count = int(input())

for _ in range(commands_count):
    command_parts = input().split(" * ")
    action = command_parts[0]

    if action == "Add Song":
        song = command_parts[1]

        if song not in playlist:
            playlist.append(song)
            print(f"{song} successfully added")

    elif action == "Delete Song":
        songs_to_delete = int(command_parts[1])

        if songs_to_delete <= len(playlist):
            deleted_songs = playlist[:songs_to_delete]
            playlist = playlist[songs_to_delete:]

            print(", ".join(deleted_songs), "deleted")

    elif action == "Shuffle Songs":
        first_index = int(command_parts[1])
        second_index = int(command_parts[2])

        if 0 <= first_index < len(playlist) and 0 <= second_index < len(playlist):
            playlist[first_index], playlist[second_index] = (
                playlist[second_index],
                playlist[first_index]
            )

            print(f"{playlist[first_index]} is swapped with {playlist[second_index]}")

    elif action == "Insert":
        song = command_parts[1]
        index = int(command_parts[2])

        if not (0 <= index < len(playlist)):
            print("Index out of range")

        elif song in playlist:
            print("Song is already in the playlist")

        else:
            playlist.insert(index, song)
            print(f"{song} successfully inserted")

    elif action == "Sort":
        playlist.sort(reverse=True)

    elif action == "Play":
        print("Songs to Play:")
        for song in playlist:
            print(song)