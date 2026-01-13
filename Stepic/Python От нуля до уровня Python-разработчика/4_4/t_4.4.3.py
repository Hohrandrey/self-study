class Multiplier:
    def __init__(self, k):
        self.k = k


    def __call__(self, x):
        return x * self.k


k = int(input())
x = int(input())
mult = Multiplier(k)
print(mult(x))
