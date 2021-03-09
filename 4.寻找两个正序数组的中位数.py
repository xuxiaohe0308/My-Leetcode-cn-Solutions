#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        idx1 = idx2 = 0
        num1 = num2 = 0
        while True:
            if idx1 + idx2 > (m+n)/2:
                break
            num1 = num2
            if idx2 >= n:
                num2 = nums1[idx1]
                idx1 += 1
                continue
            if idx1 >= m:
                num2 = nums2[idx2]
                idx2 += 1
                continue
            if nums1[idx1] > nums2[idx2]:
                num2 = nums2[idx2]
                idx2 += 1 
            else:
                num2 = nums1[idx1]
                idx1 += 1
        if (m + n) % 2 == 1:
            return num2
        else:
            return (num1 + num2) / 2
        
            
# @lc code=end

