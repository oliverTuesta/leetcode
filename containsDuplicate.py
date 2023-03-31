# https://leetcode.com/problems/contains-duplicate
# Number: 217
# Difficulty: Easy

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for i in nums:
            if i in mem:
                return True
            else:
                mem.add(i)
        return False
