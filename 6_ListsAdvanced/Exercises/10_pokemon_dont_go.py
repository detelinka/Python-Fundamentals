# Pokemon Don't Go

numbers = list(map(int, input().split()))
removed_sum = 0

while numbers:
    index = int(input())

    if index < 0:
        # remove first, copy last to its place
        removed = numbers[0]
        removed_sum += removed
        numbers[0] = numbers[-1]
    elif index >= len(numbers):
        # remove last, copy first to its place
        removed = numbers[-1]
        removed_sum += removed
        numbers[-1] = numbers[0]
    else:
        # normal case
        removed = numbers.pop(index)
        removed_sum += removed

    # adjust remaining elements
    for i in range(len(numbers)):
        if numbers[i] <= removed:
            numbers[i] += removed
        else:
            numbers[i] -= removed

print(removed_sum)