# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# Difficulty: Medium
# Number: 34

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.firstPosition(nums, target), self.lastPosition(nums, target)]

    def firstPosition(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1

        pos = -1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] == target:
                pos = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return pos
    
    def lastPosition(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1

        pos = -1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] == target:
                pos = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return pos
