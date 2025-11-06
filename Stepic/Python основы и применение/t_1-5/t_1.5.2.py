class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity - self.count - v >= 0:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.count += v

kap1 = MoneyBox(10)
kap1.add(7)
kap1.add(5)
kap1.add(100)
print(kap1.count)