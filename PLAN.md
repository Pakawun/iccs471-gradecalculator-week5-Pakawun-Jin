# Implementation plan

> This file records my project-specific steps reviewed before coding. Replace the prompts below with the agreed plan; refer to R1–R3 rather than copying the requirements here.

## Steps
1. Create `grades.py` for all calculation and grade logic, with a `SUBJECTS` dictionary holding each subject's syllabus components and weights. Create `main.py` for the command-line input and output only, and `test_grades.py` for pytest tests.
2. In `grades.py`, add `to_percentage(raw_text, max_text)` to convert a raw score and its maximum to a percentage, rejecting non-numbers, a maximum of 0 or less, and a score outside 0 to the maximum (R1). In `main.py`, list the subjects, let the user choose one, and ask for each component's score and maximum, asking again on invalid input (R1).
3. In `grades.py`, add `letter_grade(total)` using "X and above" / "below X" comparisons so decimals such as 89.99 get the correct grade (R3).
4. Turn checks C1 and C2 from EVIDENCE.md into tests in `test_grades.py`, and add tests for `to_percentage` (28 out of 30 gives 93.33; 31 out of 30, -1 out of 30, 10 out of 0 and "abc" are rejected), grade boundaries (90, 89.99, 60, 59.99), and every subject's weights adding up to 100. Run with `python3 -m pytest`.
5. Calculate my real grade for one current subject from start to finish using my actual scores, and compare the result with a manual calculation.

## Later changes, if any
Changed score input from percentages to a raw score and maximum (R1), replacing `parse_score` with `to_percentage`, because students see raw marks on their papers and should not have to convert them by hand.