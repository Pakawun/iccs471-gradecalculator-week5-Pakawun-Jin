# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work. It does not repeat setup instructions or the implementation plan.

## Concrete checks
C1–C3 were run through `main.py` with piped input; C4 and C5 were checked by the automated tests.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R1, R2, R3 — normal case | Subject ICCS471 (Assignments 30%, Midterm 30%, Final 40%) | Enter Assignments 28 out of 30, Midterm 45 out of 60, Final 70 out of 80 | `Weighted total: 85.50, Grade: B+` | Printed `Weighted total: 85.50, Grade: B+`. Pass. |
| C2 / R1 — failure case | Subject ICCS471, asking for the Assignments score | Enter 31 out of 30 | Error message saying the score must be between 0 and 30; the program asks for Assignments again | Printed "The score must be between 0 and 30." and asked for Assignments again. Pass. |
| C3 / R1 — failure case | Subject ICCS471, asking for the Assignments score | Enter `abc` as the score | Error message "Scores must be numbers."; the program asks again | Printed "Scores must be numbers." and asked for Assignments again. Pass. |
| C4 / R3 — boundary | A weighted total of 89.99, then 90 | Convert each to a letter grade | 89.99 gives B+; 90 gives A | `test_letter_grade_boundaries`: 89.99 gave B+ and 90 gave A. Pass. |
| C5 / R2 — rule | Every subject in `SUBJECTS` | Add up each subject's weights | Every subject totals exactly 100 | `test_weights_sum_to_100` passed for ICCS471, ICCS101 and ICMA201. Pass. |

## Two review decisions
- Plan decision: In PLAN.md step 2, I changed score input from a percentage to a raw score plus a maximum (replacing `parse_score` with `to_percentage`), because students see raw marks like 28/30 on their papers and should not have to convert them by hand. C1 was updated to match.
- Code decision: In `grades.py`, I accepted `letter_grade` using `>=` comparisons from the top grade down, because it matches the "X and above / below X" scale in R3 and C4 confirmed that 89.99 gives B+ and 90 gives A.

## Automated tests
- Test file and behaviour checked: `test_grades.py` checks the C1 normal case, `to_percentage` conversion and its rejection of a score above the maximum, a negative score, a maximum of 0 or less, and non-numbers (C2, C3), all letter-grade boundaries (C4), every subject's weights adding up to 100 (C5), full marks giving 100, and rounding to two decimals.
- Command I ran: `python3 -m pytest -v`.
- Final result: 32 collected, 32 passed in 0.02s.
- Correction and rerun, if needed: None needed. 

## Realistic use and final judgment
- Task I tried: Ran `python3 main.py` as a user would, choosing ICCS471 and entering Assignments 28/30, Midterm 45/60, Final 70/80, then calculated the same total by hand: 93.33×0.30 + 75×0.30 + 87.5×0.40 = 28.00 + 22.50 + 35.00 = 85.50. (These are the example marks, not my real course marks; I have not yet run my own.)
- Outcome: The program printed `Weighted total: 85.50, Grade: B+`, which matched my manual calculation of 85.50. It let me enter raw marks directly without converting them.
- Judgment: Done for the three requirements. All five concrete checks passed, all 32 automated tests passed, and the example walkthrough matched a manual calculation.
- Remaining limitation or unfinished work: An invalid score is only reported after the maximum is entered, and the user must re-enter both values. The input handling in `main.py` also has no automated tests. I have not yet tried it on real course marks.
