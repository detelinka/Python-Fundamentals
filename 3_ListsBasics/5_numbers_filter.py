n = int(input())

even = []
odd = []
negatives = []
positives = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negatives)
elif command == "positive":
    print(positives)