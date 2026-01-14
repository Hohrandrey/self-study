class Wallet:
    def __init__(self, balance = 0):
        self.__balance = balance


    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def bal_set(self, new):
        if new  < 0:
            raise ValueError("Balance cannot be negative")
        else:
            self.__balance = new

f = int(input())
s = int(input())
w = Wallet(f)
w.bal_set = s
print(f"Баланс = {w.balance}")
