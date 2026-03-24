usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16 and all(ch.isalnum() or ch in "-_" for ch in username):
        print(username)
