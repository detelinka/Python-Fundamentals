grade = float(input())

def get_grade(grade :float):
    if grade >= 5.5:
        return "Excellent"
    elif grade >= 4.5:
        return "Very Good"
    elif grade >= 3.5:
        return "Good"
    elif grade >= 3.0:
        return "Poor"
    else:
        return "Fail"

print(get_grade(grade))