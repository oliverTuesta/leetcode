# https://leetcode.com/problems/happy-number/
# Difficulty: Easy
# Number: 202

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1 and n not in mem:
            mem.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return n == 1
