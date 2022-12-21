# https://leetcode.com/problems/find-pivot-index
# Difficulty: easy

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = 0
        left = 0
        for i in range (1, len(nums)):
            right = right + nums[i]

        for i in range (0, len(nums)):
            # print(left, right)
            if (left == right):
                return i
            if (i < len(nums) - 1):
                left = left + nums[i]
                right = right - nums[i + 1]

        return -1


# print(Solution().pivotIndex([-1,-1,0,1,1,0]))
