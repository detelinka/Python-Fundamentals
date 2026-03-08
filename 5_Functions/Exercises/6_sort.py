#Write a program that receives a sequence of numbers (integers)
# separated by a single space. It should print a sorted list
# of numbers in ascending order. Use sorted().

numbers = input().split()
# turn string into a list of integers
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


print(sorted(numbers))