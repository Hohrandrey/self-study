class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = set()
        for j in range(len(nums)-1):
            for i in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.add(j)
                    res.add(i)
        return list(res)
