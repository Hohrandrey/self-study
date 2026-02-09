nums = [1, 2, 3, 4, 5, 6, 7, 8]


nd_nums = (nums[i] for i in range(0, len(nums), 2))


for _ in range(4):
    print(next(nd_nums))
