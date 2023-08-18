#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (69.93%)
# Likes:    7245
# Dislikes: 325
# Total Accepted:    1.4M
# Total Submissions: 2.1M
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
# 
# 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# 
# 
# Given n, calculate F(n).
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 30
# 
# 
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # recursion
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)

        # tabulation
        # fib_sums = [0,1]
        # for i in range(2, n+1):
        #     fib_sums.append(fib_sums[i-1] + fib_sums[i-2])
        
        # return fib_sums[n]
    
        # memoization
        # Create helper function to process fibonacci numbers
        def helper(i) -> int:
			# Basecase: Fibonacci number was found in our cache
            if i in fibMemo:
                return fibMemo[i]
            else:
				# Recursively call for the answer to our target fibonacci number
                fibMemo[i] = helper(i-1) + helper(i-2)
            return fibMemo[i]

		# Create cache by using dictionary to store past result for quick look up when recursively asking for answer to the target fibonacci number
        fibMemo = {0:0, 1:1}
		
		# Call our helper function and return the answer 
        return helper(n)
        
# @lc code=end

