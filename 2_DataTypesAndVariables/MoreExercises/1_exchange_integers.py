x = int(input())
y = int(input())

print("Before:")
print("a =", x)
print("b =", y)
x, y = y, x
print("After:")
print("a =", x)
print("b =", y)