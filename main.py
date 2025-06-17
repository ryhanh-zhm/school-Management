from services.data_manager import DataManager
from services.auth import AuthService

def main():
    data = DataManager()
    auth = AuthService(data)

    print("=== School Management System Login ===")
    username = input("Username: ")
    password = input("Password: ")

    user = auth.login(username, password)
    if user:
        print(f"Welcome, {user.name} ({user.role})")
    else:
        print("Invalid credentials")
    print("School Management System (Base Setup)")
    print("System ready. Add menu, storage, and logic to extend functionality.")

if __name__ == "__main__":
    main()