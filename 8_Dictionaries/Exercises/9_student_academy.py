n = int(input())

students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

# keep only students with avg >= 4.50 and print
for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        print(f"{name} -> {avg_grade:.2f}")