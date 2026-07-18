from random import sample

def generate_bingo():
    nums = sample(range(1, 76), 25)
    bingo = [nums[i:i+5] for i in range(0, len(nums), 5)]
    bingo[2][2] = 0
    return bingo

print(generate_bingo())