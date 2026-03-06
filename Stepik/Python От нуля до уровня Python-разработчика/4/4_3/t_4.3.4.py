class SecretData:
    def __init__(self, value):
        self.__secret = value


    @property
    def secret(self):
        return self.__secret

    @secret.deleter
    def secret(self):
        print("Элемент удалился")
        del self.__secret

o = SecretData(input())
del o.secret