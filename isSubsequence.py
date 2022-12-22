# https://leetcode.com/problems/is-subsequence/
# Number: 392
# Difficulty: Easy

class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = 0
        for c in t:
            if i >= len(s):
                break
            if s[i] == c:
                i = i + 1
        return i == len(s)
            
