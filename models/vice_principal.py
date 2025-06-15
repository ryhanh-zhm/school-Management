from .user import User

class VicePrincipal(User):
    def __init__(self, name, username=None, password=None):
        super().__init__(name, role="vice_principal", username=username, password=password)