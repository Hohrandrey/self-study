class ReversedRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __iter__(self):
        cur = self.end - 1
        while cur >= self.start:
            yield cur
            cur -= 1



start = int(input())
end = int(input())
result = [str(num) for num in ReversedRange(start, end)]
print(" ".join(result))
