num_list = input().split()

abs_values = []
for num in num_list:
    abs_values.append(abs(float(num)))

print(abs_values)