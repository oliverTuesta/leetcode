# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Difficulty: Medium
# Number: 167

class Solution(object):
    def twoSum(self, numbers, target):
        mem = {}
        for i in range(len(numbers)):
            if numbers[i] in mem:
                if numbers[i] * 2 != target:
                    continue
            t = target - numbers[i]
            if t in mem:
                return [mem[t] + 1, i + 1]
            mem[numbers[i]] = i
