class Student:
    students_id = 0

    def __init__(self, name, username, assistance=False):
        Student.students_id += 1

        self.id = Student.students_id
        self.name = name
        self.username = username
        self.assistance = assistance

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'assistance': self.assistance
        }
