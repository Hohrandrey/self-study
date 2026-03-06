class MathOperations:
    @staticmethod
    def square(x):
        return x ** 2
    @staticmethod
    def cube(x):
        return x ** 3


x = int(input())
print(MathOperations.square(x))
print(MathOperations.cube(x))
