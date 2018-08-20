"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    grade = convert_score_to_grade(float(input("Enter score: ")))
    print(grade)


def convert_score_to_grade(score):
    if score < 0 or score > 100:
        grade = 'Invalid score'
    elif score >= 90:
        grade = 'Excellent'
    elif score >= 50:
        grade = 'Passable'
    else:
        grade = 'Bad'
    return grade


main()
