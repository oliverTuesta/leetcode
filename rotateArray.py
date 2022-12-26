# https://leetcode.com/problems/rotate-array
# Difficulty: Medium
# Number: 189

class Solution(object):
    def rotate(self, nums, k):
        arr = nums[:]
        k = k % len(nums)
        j = k
        for i in range(0, len(nums)):
            nums[j] = arr[i]
            j = j + 1
            if j >= len(nums):
                j = 0
