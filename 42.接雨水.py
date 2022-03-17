#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            if leftMax <= rightMax:
                res += max(0, leftMax - height[left])
                if height[left] > leftMax: leftMax = height[left]
                left += 1
            else:
                res += max(0, rightMax - height[right])
                if height[right] > rightMax: rightMax = height[right]
                right -= 1
        return res

# @lc code=end
# Accepted
# 320/320 cases passed (44 ms)
# Your runtime beats 62.56 % of python3 submissions
# Your memory usage beats 38.47 % of python3 submissions (15.9 MB)