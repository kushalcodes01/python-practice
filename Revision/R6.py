

def check_grade(marks):

    if marks >= 90:
        return "Excellent"

    elif marks >= 60:
        return "Good"

    elif marks >= 40 :
        return "Pass"

    else:
        return "Fail"


print(check_grade(85))
print(check_grade(37))
print(check_grade(91))