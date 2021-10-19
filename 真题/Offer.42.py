'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        pre_sum = nums[0]
        for num in nums[1:]:
            pre_sum = num if num > (pre_sum + num) else pre_sum + num
            if pre_sum > max: max = pre_sum
        return max
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        pre_sum = nums[0]
        for num in nums[1:]:
            pre_sum = num if pre_sum <= 0 else pre_sum + num
            if pre_sum > max: max = pre_sum
        return max
        