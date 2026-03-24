path = input()

# Split by backslash and take the last part (file name with extension)
file_with_extension = path.split("\\")[-1]

# Split by dot into name and extension
name, extension = file_with_extension.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")
