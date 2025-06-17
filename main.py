from services.data_manager import DataManager
from services.auth import AuthService
from services.class_service import ClassService
from services.message_service import MessageService
from services.report_service import ReportService

from models.principal import Principal

def main():
    data = DataManager()
    auth = AuthService(data)

    print("=== School Management System Login ===")
    username = input("Username: ")
    password = input("Password: ")

    user = auth.login(username, password)
    if user:
        print(f"\n Welcome, {user.name} ({user.role})")
    else:
        print(" Invalid credentials")
        return

    # Services to pass to role objects
    class_service = ClassService(data)
    message_service = MessageService(data)
    report_service = ReportService(data)

    # principal
    if user.role == "principal":
        while True:
            print("\n--- Principal Menu ---")
            print("1. View all classes")
            print("2. View all messages")
            print("3. Add staff (teacher / vice_principal)")
            print("4. Generate report cards")
            print("0. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                user.view_all_classes(class_service)
            elif choice == "2":
                user.view_all_messages(message_service)
            elif choice == "3":
                role = input("Role (teacher / vice_principal): ").strip().lower()
                name = input("Name: ")
                username = input("Username: ")
                password = input("Password: ")
                user.add_staff(role, name, username, password, data)
            elif choice == "4":
                user.generate_report_cards(report_service)
            elif choice == "0":
                print("Logged out.")
                break
            else:
                print("Invalid option.")

    else:
        print("Role not implemented yet. Please add logic for other roles.")
