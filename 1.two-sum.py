#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hash_map = {}
            for i, num in enumerate(nums):
                  complement = target - num
                  if complement in hash_map:
                        # return index of complement and of current num
                        return [hash_map[complement], i]
                  else:
                        hash_map[num] = i
            return []
# @lc code=end

