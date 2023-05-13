class User:
    def __init__(self, username, password):
        self.username = username
        self.hashed_password = hash_password(password)
        self.is_authenticated = False

    def authenticate(self, password):
        if check_password(password, self.hashed_password):
            self.is_authenticated = True
            return True
        return False
