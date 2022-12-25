# https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Number: 283

class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        c = nums.count(0)
        while i < len(nums) - c:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i = i + 1

