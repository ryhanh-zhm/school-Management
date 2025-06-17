class ClassRoom:
    def __init__(self, class_id):
        self.class_id = class_id
        self.students = []
        self.subjects = []

    def add_student(self, student):
        if student.id in [s.id for s in self.students]:
            return False
        self.students.append(student)
        student.class_id = self.class_id
        return True

    def to_dict(self):
        return {
            "class_id": self.class_id,
            "students": [s.id for s in self.students],
            "subjects": self.subjects
        }

    @staticmethod
    def from_dict(data, all_students):
        classroom = ClassRoom(data["class_id"])
        classroom.students = [s for s in all_students if s.id in data["students"]]
        classroom.subjects = data.get("subjects", [])
        return classroom