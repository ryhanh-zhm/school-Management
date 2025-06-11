from .user import User

class Teacher(User):
    def __init__(self, name, username=None, password=None):
        super().__init__(name, role="teacher", username=username, password=password)
        self.subjects = []  

    def assign_subject(self, class_id, subject):
        self.subjects.append((class_id, subject))

    def to_dict(self):
        data = super().to_dict()
        data["subjects"] = self.subjects
        return data

    @classmethod
    def from_dict(cls, data):
        teacher = cls(
            name=data["name"],
            username=data.get("username"),
            password=data.get("password")
        )
        teacher.id = data.get("id", teacher.id)  #just like user class
        teacher.subjects = data.get("subjects", [])
        return teacher
