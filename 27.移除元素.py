#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        count = 0
        i = 0
        while i < l:
            while i + count <= l - 1 and nums[i+count] == val:
                count += 1
            if i + count <= l - 1: nums[i] = nums[i+count]
            i += 1
        return l - count
# @lc code=end

# Accepted
# 113/113 cases passed (40 ms)
# Your runtime beats 22.18 % of python3 submissions
# Your memory usage beats 79.48 % of python3 submissions (14.9 MB)