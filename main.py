from grades import SUBJECTS, weighted_total, to_percentage, letter_grade

def choose_subject():
    subjects = list(SUBJECTS)
    print("Subjects:")
    for number, subject in enumerate(subjects, start=1):
        print(f"  {number}) {subject}")

    while True:
        choice = input("Choose a subject number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(subjects):
            return subjects[int(choice) - 1]
        print(f"Please enter a number from 1 to {len(subjects)}.")


def ask_scores(subject):
    scores = {}
    for component, weight in SUBJECTS[subject].items():
        while True:
            try:
                raw = input(f"{component} ({weight}%) score: ")
                maximum = input(f"{component} out of: ")
                scores[component] = to_percentage(raw, maximum)
                break
            except ValueError as error:
                print(error)
    return scores

def main():
    subject = choose_subject()
    scores = ask_scores(subject)
    total = weighted_total(subject, scores)
    grade = letter_grade(total)
    print(f"Weighted total: {total:.2f}, Grade: {grade}")


if __name__ == "__main__":
    main()