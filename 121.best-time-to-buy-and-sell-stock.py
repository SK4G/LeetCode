#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (54.26%)
# Likes:    25160
# Dislikes: 793
# Total Accepted:    3.3M
# Total Submissions: 6.1M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
# 
# 
# Example 1:
# 
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
# 
# 
# Example 2:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # max_profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r += 1
        
        # return max_profit

        # set lowest price to first num in array.
        # iterate through prices. if lower price is found update lowest price
        # if higher profit is found update max_profit
        lowest = prices[0]
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > max_profit:
                max_profit = price - lowest
        return max_profit
        
# @lc code=end

