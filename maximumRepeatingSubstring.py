# https://leetcode.com/problems/maximum-repeating-substring/ 
# Difficulty: Easy
# Number: 1668

class Solution(object):
    def maxRepeating(self, sequence, word):
        k = 0
        for i in range(0, len(sequence) - len(word) + 1):
            c = 0
            for j in range(i, len(sequence) - len(word) + 1, len(word)):
                if sequence[j:j+len(word)] == word:
                    c = c + 1
                else:
                    break
            k = max(k, c)

        return k

