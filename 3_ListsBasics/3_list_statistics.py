n = int(input())

positives = []
negatives = []

sum_positive = 0
sum_negative = 0

for _ in range(n):
    n = int(input())

    if n >= 0:
        positives.append(n)
    else:
        negatives.append(n)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')