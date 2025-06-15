import uuid

class User:
    def __init__(self, name, role, username=None, password=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.role = role
        self.username = username or self.generate_username()
        
        if password:
            self.validate_password(password)
            self.password = password
        else:
            self.password = self.generate_password()

    def generate_username(self):
        return self.name.lower().replace(" ", "") + self.id[:4]

    def generate_password(self):
        return uuid.uuid4().hex[:8] #By the system default

    def validate_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

    def change_password(self, new_password):
        self.validate_password(new_password)
        self.password = new_password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "username": self.username,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            name=data["name"],
            role=data["role"],
            username=data["username"],
            password=data["password"]
        )
        user.id = data.get("id", user.id) # To avoid generating a new ID each time, the previous ID will be used if it already exists.
        return user
    
    def __repr__(self):
        return f"<User {self.username} ({self.role})>"

# Uuid and classmethods has been tought in our advnaced class.
# The hex() function in Python is used to convert an integer to its hexadecimal representation. The function returns a string that starts with the prefix "0x" followed by the hexadecimal value.