def grade(marks):
    if marks >=90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "You are in trouble"
print(grade(99))
print(grade(78))
print(grade(88))