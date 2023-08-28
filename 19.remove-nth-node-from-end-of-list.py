#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (41.34%)
# Likes:    15967
# Dislikes: 669
# Total Accepted:    2.1M
# Total Submissions: 4.9M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# Follow up: Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp_head = ListNode(0, head)
        left = tmp_head
        right = head

        # advance right pointer to be n nodes away from left pointer
        while n > 0:
            right = right.next
            n -= 1

        # advance both pointer at same pace until right pointer is at the end
        while right:
            right = right.next
            left = left.next
        
        # delete nth node
        left.next = left.next.next
        return tmp_head.next
        
        
# @lc code=end