from typing import List
from School import Student
class Group:
    students_list: List[Student]

    def __init__(self, students_list):
        self.students_list = students_list

    def add_student(self, new_student: Student):
        return self.students_list.append(new_student)

    def group_average_grade(self):
        group_total = 0.0
        for i in self.students_list:
            group_total += i.calc_grade_average()

        return group_total / len(self.students_list)