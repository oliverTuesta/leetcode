# https://leetcode.com/problems/spiral-matrix/
# Difficulty: Medium
# Number: 54

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mem = set()
        h = len(matrix)
        w = len(matrix[0])
        n = h * w
        i = j = 0
        arr = []
        while len(arr) < n:
            while j < w and (i, j) not in mem:
                arr.append(matrix[i][j])
                mem.add((i, j))
                j += 1
            j -= 1
            i += 1
            while i < h and (i, j) not in mem:
                arr.append(matrix[i][j])
                mem.add((i, j))
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and (i, j) not in mem:
                arr.append(matrix[i][j])
                mem.add((i, j))
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and (i, j) not in mem:
                arr.append(matrix[i][j])
                mem.add((i, j))
                i -= 1
            i += 1
            j += 1
        return arr
