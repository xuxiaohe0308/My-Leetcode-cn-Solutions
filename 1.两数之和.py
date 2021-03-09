#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if (target - num in list(hash_table.keys())) and hash_table[target-num] != i:
                return [i, hash_table[target-num]]
            hash_table[num] = i
        return [-1, -1]
# @lc code=end

