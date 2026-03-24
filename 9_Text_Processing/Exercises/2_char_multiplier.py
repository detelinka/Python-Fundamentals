str1, str2 = input().split()

total_sum = 0
len1, len2 = len(str1), len(str2)
min_len = min(len1, len2)

# multiply common length chars
for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

# add remaining chars from the longer string
if len1 > len2:
    for i in range(min_len, len1):
        total_sum += ord(str1[i])
elif len2 > len1:
    for i in range(min_len, len2):
        total_sum += ord(str2[i])

print(total_sum)
