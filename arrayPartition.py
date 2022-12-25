# https://leetcode.com/problems/array-partition/
# Difficulty: Easy
# Number: 561

class Solution(object):
    def arrayPairSum(self, nums):
        sorted_nums = sorted(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum = sum + sorted_nums[i]
        return sum
