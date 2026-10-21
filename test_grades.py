import pytest

from grades import SUBJECTS, letter_grade, to_percentage, weighted_total


# C1 / R1, R2, R3 - normal case
def test_normal_case_iccs471():
    scores = {
        "Assignments": to_percentage("28", "30"),
        "Midterm": to_percentage("45", "60"),
        "Final": to_percentage("70", "80"),
    }
    total = weighted_total("ICCS471", scores)
    assert total == 85.50
    assert letter_grade(total) == "B+"


# to_percentage
def test_to_percentage_valid():
    assert round(to_percentage("28", "30"), 2) == 93.33
    assert to_percentage("0", "30") == 0
    assert to_percentage("30", "30") == 100


# C2 / R1 - score above maximum
def test_score_above_maximum_rejected():
    with pytest.raises(ValueError, match="between 0 and 30"):
        to_percentage("31", "30")


def test_negative_score_rejected():
    with pytest.raises(ValueError, match="between 0 and 30"):
        to_percentage("-1", "30")


@pytest.mark.parametrize("maximum", ["0", "-10"])
def test_non_positive_maximum_rejected(maximum):
    with pytest.raises(ValueError, match="greater than 0"):
        to_percentage("10", maximum)


# C3 / R1 - non-numbers
@pytest.mark.parametrize("raw, maximum", [("abc", "30"), ("10", "abc"), ("", "30")])
def test_non_numbers_rejected(raw, maximum):
    with pytest.raises(ValueError, match="Scores must be numbers."):
        to_percentage(raw, maximum)


# C4 / R3 - boundaries
@pytest.mark.parametrize(
    "total, expected",
    [
        (100, "A"),
        (90, "A"),
        (89.99, "B+"),
        (85, "B+"),
        (84.99, "B"),
        (80, "B"),
        (79.99, "C+"),
        (75, "C+"),
        (74.99, "C"),
        (70, "C"),
        (69.99, "D+"),
        (65, "D+"),
        (64.99, "D"),
        (60, "D"),
        (59.99, "F"),
        (0, "F"),
    ],
)
def test_letter_grade_boundaries(total, expected):
    assert letter_grade(total) == expected


# C5 / R2 - weights add up to 100
@pytest.mark.parametrize("subject", list(SUBJECTS))
def test_weights_sum_to_100(subject):
    assert sum(SUBJECTS[subject].values()) == 100


@pytest.mark.parametrize("subject", list(SUBJECTS))
def test_full_marks_give_100(subject):
    scores = {component: 100 for component in SUBJECTS[subject]}
    assert weighted_total(subject, scores) == 100


def test_weighted_total_rounded_to_two_decimals():
    scores = {"Assignments": 93.3333333, "Midterm": 75, "Final": 87.5}
    assert weighted_total("ICCS471", scores) == 85.5
