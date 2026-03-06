class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


    @classmethod
    def from_string(cls, user_string):
        username, email = user_string.split(',')
        return User(username, email)


user_data = "alice,alice@example.com"
user = User.from_string(user_data)
print(user.username, user.email)
