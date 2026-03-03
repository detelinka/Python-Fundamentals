numbers = [int(x) for x in input().split(", ")]
beggars_count = int(input())

result = []

for i in range(beggars_count):
    # take every i-th element starting from index i
    current_sum = sum(numbers[i::beggars_count])
    result.append(current_sum)

print(result)