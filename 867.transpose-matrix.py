#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (64.56%)
# Likes:    2919
# Dislikes: 425
# Total Accepted:    256.2K
# Total Submissions: 393.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a 2D integer array matrix, return the transpose of matrix.
# 
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        len_row = len(matrix)
        len_col = len(matrix[0])

        res = [[0 for i in range(len_row)] for j in range(len_col)]
        
        for row in range(len_row):
            for col in range(len_col):
                res[col][row] = matrix[row][col]
        return res

# @lc code=end

