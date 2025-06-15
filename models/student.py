from .user import User

class Student(User):
    def __init__(self, name, username=None, password=None):
        super().__init__(name, role="student", username=username, password=password)
        self.class_id = None
        self.parent_id = None
        self.grades = {}
        self.disciplinary = []

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "class_id": self.class_id,
            "parent_id": self.parent_id,
            "grades": self.grades,
            "disciplinary": self.disciplinary
        })
        return data

    @classmethod
    def from_dict(cls, data):
        student = cls(
            name=data["name"],
            username=data.get("username"),
            password=data.get("password")
        )
        student.id = data.get("id", student.id)  # Just as user class
        student.class_id = data.get("class_id")
        student.parent_id = data.get("parent_id")
        student.grades = data.get("grades", {})
        student.disciplinary = data.get("disciplinary", [])
        return student
    
    def __repr__(self):
       return f"<Student {self.username} | Class: {self.class_id}>"
