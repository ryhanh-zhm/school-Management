import json
import os
from models.classroom import ClassRoom

DATA_FILE = "data/classes.json"

class ClassService:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.file_path = DATA_FILE
        self.classes = []
        self.load_classes()

    def load_classes(self):
        if not os.path.exists(self.file_path):
            self.classes = []
            return
        with open(self.file_path, "r") as f:
            data = json.load(f)
        self.classes = [ClassRoom.from_dict(c, self.data_manager.users) for c in data]

    def save_classes(self):
        with open(self.file_path, "w") as f:
            json.dump([c.to_dict() for c in self.classes], f, indent=4)

    def create_class(self, class_id):
        if any(c.class_id == class_id for c in self.classes):
            return False
        new_class = ClassRoom(class_id)
        self.classes.append(new_class)
        self.save_classes()
        return True

    def assign_student_to_class(self, student, class_id):
        for c in self.classes:
            if student in c.students:
                c.students.remove(student)
        for c in self.classes:
            if c.class_id == class_id:
                result = c.add_student(student)
                self.save_classes()
                self.data_manager.save_data()
                return result
        return False

    def get_class_by_id(self, class_id):
        return next((c for c in self.classes if c.class_id == class_id), None)

    def list_classes(self):
        return self.classes