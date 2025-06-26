class Student:
    name: str
    id: int
    grade_list: list
    
    def __init__(self, name, id, grade_list):
        self.name = name
        self.id = id
        self.grade_list = grade_list
    
    def add_grade(self, new_grade):
        return self.grade_list.append(new_grade)

    def calc_grade_average(self):
        return sum(self.grade_list) / len(self.grade_list)

    def show_data(self):
        print(f"""
        Name: {self.name}
        Id: {self.id}
        Grades: {self.grade_list}
        """)

