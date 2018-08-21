"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    grade = convert_score_to_grade(float(input("Enter score: ")))
    print(grade)


def convert_score_to_grade(score):
    if score < 0 or score > 100:
        return 'Invalid score'
    elif score >= 90:
        return 'Excellent'
    elif score >= 50:
        return 'Passable'
    else:
        return 'Bad'


main()
