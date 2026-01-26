text = input()

while text != "End":

    if text != "SoftUni":
        result = ""
        for char in text: result += char * 2
        print(result)

    text = input()