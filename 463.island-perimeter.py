#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (69.72%)
# Likes:    5879
# Dislikes: 291
# Total Accepted:    448.8K
# Total Submissions: 642.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0]]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N, p = len(grid), len(grid[0]), 0
        for m in range(M):
              for n in range(N):
                    if grid[m][n] == 1:
                        if m == 0   or grid[m-1][n] == 0: p += 1
                        if n == 0   or grid[m][n-1] == 0: p += 1
                        if n == N-1 or grid[m][n+1] == 0: p += 1
                        if m == M-1 or grid[m+1][n] == 0: p += 1

        return p
        
# @lc code=end

