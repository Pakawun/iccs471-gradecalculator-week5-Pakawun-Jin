# Grade Calculator

> This file explains who the project is for, what it should do, and how to run it.

## Purpose
A command-line tool for students who want to enter their raw marks for a course and see their weighted total and letter grade, based on that course's syllabus, without converting anything by hand.

## Requirements
- R1: The user chooses a subject from a list, and for each graded component enters the raw score and the maximum possible score (for example 28 out of 30). The program converts it to a percentage. The maximum must be greater than 0 and the score must be between 0 and the maximum; invalid values or non-numbers are rejected with an error message and asked again.
- R2: The program calculates the weighted total using that subject's component weights (each percentage multiplied by its weight, summed) and shows it rounded to two decimal places. Each subject's weights must add up to exactly 100.
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

## Setup and use
- Prerequisites: Python 3.10 or newer; pytest (for tests only).
- Setup: `git clone https://github.com/Pakawun/iccs471-gradecalculator-week5-Pakawun-Jin.git`, then `cd iccs471-gradecalculator-week5-Pakawun-Jin`, then `python3 -m venv .venv`, then `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`), then `pip install -r requirements.txt`.
- Run: `python3 main.py`, choose a subject, then enter each component's score and its maximum. Example: choose `1` (ICCS471), enter Assignments `28` out of `30`, Midterm `45` out of `60`, Final `70` out of `80`, and the program prints `Weighted total: 85.50, Grade: B+`.
- Run tests: `python3 -m pytest`

## Author and acknowledgements
- Name / student ID: Pakawun Jindawat 6681453
- AI tools used: GitHub Copilot, Claude Code
- External code/resources: None

See PLAN.md for the implementation plan and EVIDENCE.md for results and decisions.