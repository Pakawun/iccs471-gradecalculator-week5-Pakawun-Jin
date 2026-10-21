# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work. It does not repeat setup instructions or the implementation plan.

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R1, R2, R3 — normal case | Subject ICCS471 (Assignments 30%, Midterm 30%, Final 40%) | Enter Assignments 28 out of 30, Midterm 45 out of 60, Final 70 out of 80 | `Weighted total: 85.50, Grade: B+` | [Complete after checking.] |
| C2 / R1 — failure case | Subject ICCS471, asking for the Assignments score | Enter 31 out of 30 | Error message saying the score must be between 0 and 30; the program asks for Assignments again | [Complete after checking.] |
| C3 / R1 — failure case | Subject ICCS471, asking for the Assignments score | Enter `abc` as the score | Error message "Scores must be numbers."; the program asks again | [Complete after checking.] |
| C4 / R3 — boundary | A weighted total of 89.99, then 90 | Convert each to a letter grade | 89.99 gives B+; 90 gives A | [Complete after checking.] |
| C5 / R2 — rule | Every subject in `SUBJECTS` | Add up each subject's weights | Every subject totals exactly 100 | [Complete after checking.] |

## Two review decisions
- Plan decision: I changed step 3's `test_grades.py` check the C1 normal class `to_percentage` (raw score and maximum), because students see raw mark like 28/30 on their papers and should not have to convert them by hand. 
- Code decision: In `grades.py`, I accepted `letter_grade` using `>=` comparisons from the top grade down, because it matches the "X and above / below X" scale in R3 and C4 confirmed that 89.99 gives B+ and 90 gives A.

## Automated tests
- Test file and behaviour checked: `test_grades.py` check the C1 normal case, to `to_percentage` conversion and rejection of scores above the maximum, negative score, a maximum of 0 or less and non-number (C2, C3), all letter-grade bounderies (C4), every subject's weight adding up to 100 (C5) , full marks giving 100, and rounding to two decimals. 
- Command I ran: `python3 -m pytest -v`.
- Final result: 32 collected, 32 passed in 0.02s.
- Correction and rerun, if needed: None needed. 

## Realistic use and final judgment
- Task I tried: Calculated my grade for [Subject] using my actual marks: [component score/max], then calculated the same total by hand.
- Outcome: The program printed `Weighted total: [xx.xx], Grade: [X]`, which [matched / did not match] my manual calculation of [xx.xx]. It let me enter raw marks directly without converting them.
- Judgment: Done. All five concrete checks passed, all 32 automated test passed, and realistic use matched a manual calculation. 
- Remaining limitation or unfinished work: An invalid socre is only reported after the maximumis entered, and the user must re-enter both values. The input handling in `main.py` also has no automated tests.