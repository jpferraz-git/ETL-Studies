import School

from Group import Group
# student1 = School.Student("Michael", "001",[8.8, 7.9])
#
# student1.add_grade(9.3)
# student1.calc_grade_average()
# student1.show_data()

s1 = School.Student("João", 101, [8.0, 9.0, 7.5])
s2 = School.Student("Maria", 102, [6.5, 7.0, 8.5])
grupo = Group([s1, s2])

media_grupo = grupo.group_average_grade()
print(f"Média da turma: {media_grupo:.2f}")