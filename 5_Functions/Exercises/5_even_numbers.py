def is_even(current_num: int) -> bool:
    return current_num % 2 == 0

string = input().split()
nums = []

for num in string:
    nums.append(int(num))

result = filter(is_even, nums)
print(list(result))