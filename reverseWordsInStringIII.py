# https://leetcode.com/problems/reverse-words-in-a-string-iii
# Difficulty: Easy
# Number: 557

class Solution(object):
    def reverseWords(self, s):
        rs = ""
        for word in s.split():
            rs = rs + ''.join(reversed(word)) + " "
        return rs.rstrip()
