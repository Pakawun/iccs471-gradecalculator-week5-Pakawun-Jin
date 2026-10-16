# Implementation plan

> This file records my project-specific steps reviewed before coding. Replace the prompts below with the agreed plan; refer to R1–R3 rather than copying the requirements here.

## Steps
1. Create `grades.py` for all calculation and grade logic, with a `SUBJECTS` dictionary holding each subject's syllabus components and weights. Create `main.py` for the command-line input and output only, and `test_grades.py` for pytest tests.
2. In `main.py`, list the subjects, let the user choose one, and ask for a score for each of that subject's components (R1). In `grades.py`, add `weighted_total(subject, scores)` to multiply each score by its weight, sum them, and round to two decimal places (R2).
3. In `grades.py`, add `parse_score(text)` to reject non-numbers and scores outside 0–100 with an error message, so `main.py` asks again (R3). Add `letter_grade(total)` using "X and above" / "below X" comparisons so decimals such as 89.99 get the correct grade (R3).
4. Turn checks C1 (normal weighted total) and C2 (out-of-range score) from EVIDENCE.md into tests in `test_grades.py`, and add tests for grade boundaries (90, 89.99, 60, 59.99), scores of 0 and 100, non-numeric input, and every subject's weights adding up to 100. Run with `python3 -m pytest`.
5. Calculate my real grade for one current subject from start to finish using my actual scores, and compare the result with a manual calculation.

## Later changes, if any
not yet