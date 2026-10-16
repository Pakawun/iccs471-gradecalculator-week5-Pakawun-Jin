SUBJECTS = {
    "ICCS471": {"Assignments": 30, "Midterm": 30, "Final": 40},
    "ICCS101": {"Quizzes": 20, "Labs": 20, "Midterm": 25, "Final": 35},
    "ICMA201": {"Homework": 20, "Midterm": 40, "Final": 40},
}


def weighted_total(subject, scores):
    weights = SUBJECTS[subject]
    total = sum(scores[component] * weight / 100 for component, weight in weights.items())
    return round(total, 2)


def to_percentage(raw_text, max_text):
    try:
        raw = float(raw_text)
        maximum = float(max_text)
    except ValueError:
        raise ValueError("Scores must be numbers.")
    if maximum <= 0:
        raise ValueError("The maximum score must be greater than 0.")
    if not 0 <= raw <= maximum:
        raise ValueError(f"The score must be between 0 and {maximum:g}.")
    return raw / maximum * 100


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
