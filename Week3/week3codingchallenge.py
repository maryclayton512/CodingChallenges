class Student():
    def __init__(self, student_id, student_name):
        self._student_id = student_id
        self.student_name = student_name
        self.student_list = []
    def add_student(self, student_id, student_name):
        self.student_list.append(student_id, student_name)
