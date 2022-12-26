# https://leetcode.com/problems/longest-palindrome
# Difficulty: Easy
# Number: 409

class Solution(object):
    def longestPalindrome(self, s):
        letters = dict()
        for c in s:
            letters[c] = letters.get(c, 0) + 1

        single = False
        lp = 0
        for k, v in letters.items():
            lp = lp + v
            if v % 2 != 0:
                lp = lp - 1
                single = True
        if single:
            lp = lp + 1
        return lp
