n = int(input())

filled = n // 10
dots = 10 - filled
bar = "%" * filled + "." * dots

if n == 100:
    print(f"100% Complete!")
    print(f"[{bar}]")
else:
    print(f"{n}% [{bar}]")
    print("Still loading...")