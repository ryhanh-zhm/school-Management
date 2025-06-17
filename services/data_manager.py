import json
import os
from models.student import Student
from models.teacher import Teacher
from models.parent import Parent
from models.principal import Principal
from models.vice_principal import VicePrincipal

DATA_FILE = "data/users.json"

class DataManager:
    def __init__(self, file_path=DATA_FILE):
        self.file_path = file_path
        self.users = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            self.users = []
            return
        with open(self.file_path, "r") as f:
            data = json.load(f)
        self.users = [self._create_user_from_dict(u) for u in data]

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4)

    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def find_user_by_username(self, username):
        return next((u for u in self.users if u.username == username), None)

    def _create_user_from_dict(self, data):
        role = data["role"]
        if role == "student":
            return Student.from_dict(data)
        elif role == "teacher":
            return Teacher.from_dict(data)
        elif role == "parent":
            return Parent.from_dict(data)
        elif role == "principal":
            return Principal(data["name"], data["username"], data["password"])
        elif role == "vice_principal":
            return VicePrincipal(data["name"], data["username"], data["password"])
        else:
            raise ValueError(f"Unknown role: {role}")
