def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1]


numbers = input().split(", ")
for num in numbers:
    print(is_palindrome(int(num)))
