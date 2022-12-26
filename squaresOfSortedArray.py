# https://leetcode.com/problems/squares-of-a-sorted-array
# Difficulty: Easy
# Number: 977

class Solution(object):
    def sortedSquares(self, nums):
        squares = []
        for i in nums:
            squares.append(i*i)
        squares.sort()
        return squares
