# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Number: 3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = set()
        max_lenght = 0
        for i, c in enumerate(s):
            if c in chars:
                while c in chars:
                    chars.remove(s[i - len(chars)])
            chars.add(c)
            max_lenght = max(max_lenght, len(chars))
        return max_lenght
