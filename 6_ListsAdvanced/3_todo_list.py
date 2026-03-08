todo_list = []

while True:
    task = input()
    if task == "End":
        break

    importance, note = task.split("-")
    importance = int(importance)

    # намираме къде да вмъкнем (сортиране чрез insert)
    inserted = False
    for i in range(len(todo_list)):
        if importance < todo_list[i][0]:
            todo_list.insert(i, [importance, note])
            inserted = True
            break

    if not inserted:
        todo_list.append([importance, note])

# правим списък само с бележките в правилния ред
result = []

while todo_list:
    item = todo_list.pop(0)   # използваме pop
    result.append(item[1])

print(result)
