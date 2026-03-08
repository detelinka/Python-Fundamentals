n = int(input())

if n == 100:
    print(f"{n}%", end="" " Complete!")
    print()
    print("[%%%%%%%%%%]")

else:
    print(f"{n}% ", end="[")
    print("%" * (n // 10), end="")
    print("." * ((100 - n) // 10), end="]")
    print()
    print(f"Still loading...")
