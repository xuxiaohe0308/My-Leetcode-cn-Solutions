#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DP，背包问题
        # 初始状态设为全负，和为neg_sum
        # 正记为“选取”，目标为(target - neg_sum) / 2
        neg_sum = sum(nums) * -1
        target = (target - neg_sum) / 2
        if target != round(target) or target < 0:
            return 0
        else:
            target = int(target)
        n_nums = len(nums)
        mat = [ [0 for _ in range(target+1)] for _ in range(n_nums) ]

        n = nums[0]
        mat[0][0] = 1 if n > 0 else 2
        for j in range(1, target+1):
            if j == n:
                mat[0][j] = 1

        # 状态转移
        for i in range(1, n_nums):
            n = nums[i]
            for j in range(target+1):
                if n > j:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i-1][j] + mat[i-1][j-n]
        return mat[n_nums-1][target]
# @lc code=end

