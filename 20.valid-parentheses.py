#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.42%)
# Likes:    19797
# Dislikes: 1174
# Total Accepted:    3.3M
# Total Submissions: 8.2M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        close_pair = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c in close_pair:
                if stack and stack[-1] == close_pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack 
        
# @lc code=end

