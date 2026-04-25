def encrypt(message: str) -> str:
    return message[::-1]

def decrypt(message: str) -> str:
    return ''.join(
        ch.lower() if ch.isupper() else ch.upper()
        for ch in message
    )

def substitute(message: str, old_char: str, new_char: str):
    if old_char not in message:
        print("Character not found.")
        return message
    message = message.replace(old_char, new_char)
    print(message)
    return message

def scramble(message: str, index: int, char: str):
    if index < 0 or index >= len(message):
        print("Index out of bounds.")
        return message
    message = message[:index] + char + message[index + 1:]
    print(message)
    return message

def remove_substring(message: str, substring: str):
    message = message.replace(substring, "")
    print(message)
    return message

def main():
    message = input()

    while True:
        line = input()
        if line == "Finalize":
            break

        parts = line.split()
        command = parts[0]

        if command == "Encrypt" and len(parts) == 1:
            message = encrypt(message)
            print(message)

        elif command == "Decrypt" and len(parts) == 1:
            message = decrypt(message)
            print(message)

        elif command == "Substitute" and len(parts) == 3:
            old_char = parts[1]
            new_char = parts[2]
            message = substitute(message, old_char, new_char)

        elif command == "Scramble" and len(parts) == 3:
            index_str = parts[1]
            char = parts[2]

            try:
                index = int(index_str)
            except ValueError:
                print("Invalid command detected!")
                continue

            message = scramble(message, index, char)

        elif command == "Remove" and len(parts) == 2:
            substring = parts[1]
            message = remove_substring(message, substring)

        else:
            print("Invalid command detected!")

if __name__ == "__main__":
    main()