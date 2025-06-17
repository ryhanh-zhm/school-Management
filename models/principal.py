from .user import User
from models.teacher import Teacher
from models.vice_principal import VicePrincipal

class Principal(User):
    def __init__(self, name, username=None, password=None):
        super().__init__(name, role="principal", username=username, password=password)

    def view_all_classes(self, class_service):
        print("\n Class List with Student Counts:")
        for cls in class_service.classes:
            print(f" - Class {cls.class_id}: {len(cls.students)} students")

    def view_all_messages(self, message_service):
        print("\nAll Messages:")
        messages = message_service.get_all_messages()
        if not messages:
            print("No messages.")
            return
        for msg in messages:
            print(f"\nFrom: {msg.sender} -> To: {msg.receiver}")
            print(f"Message: {msg.content}")

    def add_staff(self, role, name, username, password, data_manager):
        if any(u.username == username for u in data_manager.users):
            print("Username already exists.")
            return

        if role == "teacher":
            new_user = Teacher(name, username, password)
        elif role == "vice_principal":
            new_user = VicePrincipal(name, username, password)
        else:
            print("Invalid role.")
            return

        data_manager.users.append(new_user)
        data_manager.save_users()
        print(f"{role.capitalize()} '{name}' added successfully.")

    def generate_report_cards(self, report_service):
        success = report_service.generate_all()
        if success:
            print("Report cards generated successfully.")
        else:
            print("Some students are missing grades. Report card generation failed.")
