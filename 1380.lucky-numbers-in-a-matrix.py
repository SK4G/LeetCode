#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
#
# algorithms
# Easy (70.67%)
# Likes:    1514
# Dislikes: 76
# Total Accepted:    89K
# Total Submissions: 125.8K
# Testcase Example:  '[[3,7,8],[9,11,13],[15,16,17]]'
#
# Given an m x n matrix of distinct numbers, return all lucky numbers in the
# matrix in any order.
# 
# A lucky number is an element of the matrix such that it is the minimum
# element in its row and maximum in its column.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row
# and the maximum in its column.
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row
# and the maximum in its column.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row
# and the maximum in its column.
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 10^5.
# All elements in the matrix are distinct.
# 
# 
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lrow = len(matrix)
        lcol = len(matrix[0])
        lucky_numbers = []
        
        for i in range(lrow):
            # find min in row
            min_row = min(matrix[i])
            # find col index of min row
            min_col_idx = matrix[i].index(min_row)
            max_col = max(matrix[row][min_col_idx] for row in range(lrow))
            
            if min_row == max_col:
                lucky_numbers.append(min_row)

        return lucky_numbers
# @lc code=end

