# https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Number: 704

class Solution(object):
    def search(self, nums, target):

        def binarySearch(left, right, target):
            if (left > right):
                return -1
            m = (left + right) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                return binarySearch(left, m-1, target)
            else:
                return binarySearch(m+1, right, target)

        return binarySearch(0, len(nums)-1, target)


