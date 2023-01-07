# https://leetcode.com/problems/where-will-the-ball-fall/
# Difficulty: Medium
# Number: 1706

class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        self.mem = dict()
        self.grid = grid
        ans = []
        for j in range(0, len(grid[0])):
            ans.append(self.dropBall(0, j))
        return ans
    
    def dropBall(self, i: int, j: int) -> int:
        if (i, j) in self.mem:
            return self.mem[(i, j)]
        if i >= len(self.grid):
            return j
        elif j >= len(self.grid[0]):
            return -1
        current = self.grid[i][j]
        if j + current < 0 or j + current >= len(self.grid[0]):
            self.mem[(i, j)] = -1
            return -1
        beside = self.grid[i][j + current]

        if current == beside:
            self.mem[(i, j)] = self.dropBall(i + 1, j + current)
        else:
            self.mem[(i, j)] = -1
        return self.mem[(i, j)]
