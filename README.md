# Grade Calculator

> This file explains who the project is for, what it should do, and how to run it.

## Purpose
A command-line tool for students who want to enter their assignment scores and quickly see their average and letter grade.

## Requirements
- R1: The user enters a score (0–100) for each graded component in the course syllabus:

  | Component | Weight |
  |---|---|
  | Assignments | 30% |
  | Midterm exam | 30% |
  | Final exam | 40% |

- R2: The program calculates the weighted total score, where each component's score is multiplied by its weight, and shows it rounded to two decimal places.
- R3: The program converts the weighted total to a letter grade using this scale:

  | Grade | Weighted total |
  |---|---|
  | A | 90 and above |
  | B+ | 85 to below 90 |
  | B | 80 to below 85 |
  | C+ | 75 to below 80 |
  | C | 70 to below 75 |
  | D+ | 65 to below 70 |
  | D | 60 to below 65 |
  | F | below 60 |

  Each score must be between 0 and 100; a score outside this range or a non-number is rejected with an error message and asked again, and the component weights must add up to exactly 100%.

## Setup and use
- Prerequisites: Python 3.10 or newer; pytest (for tests only).
- Setup: `git clone https://github.com/Pakawun/iccs471-gradecalculator-week5-Pakawun-Jin.git`, then `cd iccs471-gradecalculator-week5-Pakawun-Jin`, then `python3 -m venv .venv`, then `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`), then `pip install -r requirements.txt`.
- Run: `python3 main.py`, then enter scores one per line and type `done` to finish. Example: enter `80`, `90`, then `done`, and the program prints `Average: 85.00, Grade: A`.
- Run tests: `python3 -m pytest`

## Author and acknowledgements
- Name / student ID: Pakawun Jindawat 6681453
- AI tools used: GitHub Copilot and Claude code
- External code/resources: None

See PLAN.md for the implementation plan and EVIDENCE.md for results and decisions.