SUBJECTS = {
    "ICCS471": {"Assignments": 30, "Midterm": 30, "Final": 40},
    "ICCS101": {"Quizzes": 20, "Labs": 20, "Midterm": 25, "Final": 35},
    "ICMA201": {"Homework": 20, "Midterm": 40, "Final": 40},
}


def weighted_total(subject, scores):
    weights = SUBJECTS[subject]
    total = sum(scores[component] * weight / 100 for component, weight in weights.items())
    return round(total, 2)


def letter_grade(total):

    print(f"Total Score: {total}")

    if total >= 90:
        return "Grade: A"
    if total >= 85:
        return "Grade: B+"
    if total >= 80:
        return "Grade: B"
    if total >= 75:
        return "Grade: C+"
    if total >= 70:
        return "Grade: C"
    if total >= 65:
        return "Grade: D+"
    if total >= 60:
        return "Grade: D"
    return "Grade: F"


total = weighted_total("ICCS471", {"Assignments": 28, "Midterm": 25, "Final": 35})
grade = letter_grade(total)
print(grade)
