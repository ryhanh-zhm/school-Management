from .user import User

class Parent(User):
    def __init__(self, name, username=None, password=None):
        super().__init__(name, role="parent", username=username, password=password)
        self.student_id = None

    def to_dict(self):
        data = super().to_dict()
        data["student_id"] = self.student_id
        return data

    @classmethod
    def from_dict(cls, data):
        parent = cls(data["name"], data["username"], data["password"])
        parent.student_id = data.get("student_id")
        return parent