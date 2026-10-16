SUBJECTS = {
    "ICCS471": {"Assignments": 30, "Midterm": 30, "Final": 40},
    "ICCS101": {"Quizzes": 20, "Labs": 20, "Midterm": 25, "Final": 35},
    "ICMA201": {"Homework": 20, "Midterm": 40, "Final": 40},
}


def weighted_total(subject, scores):
    weights = SUBJECTS[subject]
    total = sum(scores[component] * weight / 100 for component, weight in weights.items())
    return round(total, 2)

# print(weighted_total("ICCS471", {"Assignments": 85, "Midterm": 90, "Final": 80}))  # Example usage