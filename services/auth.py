class AuthService:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def login(self, username, password):
        user = self.data_manager.find_user_by_username(username)
        if user and user.password == password:
            return user
        return None

    def change_password(self, user, new_password):
        user.change_password(new_password)
        self.data_manager.save_data()
