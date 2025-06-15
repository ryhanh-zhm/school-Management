from .user import User

class Principal(User):
    def __init__(self, name, username=None, password=None):
        super().__init__(name, role="principal", username=username, password=password)