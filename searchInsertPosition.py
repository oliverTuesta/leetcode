# https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Number: 35

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else: 
                r = m

        m = (l + r) // 2
        ans = m
        if nums[m] < target:
            ans = m + 1

        return ans

