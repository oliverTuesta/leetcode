# https://leetcode.com/problems/first-bad-version/
# Difficulty: Easy
# Number: 278

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(n):
    return n >= 4

class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else: 
                l = m + 1
        return (l + r) // 2


