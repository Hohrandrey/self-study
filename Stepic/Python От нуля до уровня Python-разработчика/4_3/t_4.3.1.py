class UserProfile:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self._email = email
        self.__password = password


    def check_password(self, password: str) -> bool:
        if password == self.__password:
            return True
        return False


    def change_password(self, old: str, new: str):
        if self.check_password(old):
            self.__password = new


    def get_password(self) -> str:
        return self.__password


username = input()
email = input()
password = input()
old = input()
new = input()


usprof = UserProfile(username, email, password)
usprof.change_password(old, new)
print(f"Username: {usprof.username}, email: {usprof._email}, password: {usprof.get_password()}")