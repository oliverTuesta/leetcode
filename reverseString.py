# https://leetcode.com/problems/reverse-string/
# Difficulty: Easy
# Number: 344

class Solution(object):
    def reverseString(self, s):
        r = len(s) - 1
        for l in range(0, len(s) // 2):
            s[l], s[r] = s[r], s[l]
            r = r - 1

