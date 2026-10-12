from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_stu = None
    highest_marks = 0

    for name, marks in scores:
        if marks > highest_marks:
            highest_marks = marks
            best_stu = name
    return best_stu


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
