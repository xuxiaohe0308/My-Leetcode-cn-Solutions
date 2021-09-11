#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        ret = [[_ for _ in range(amount+1)] for _ in range(m)]  # m * amount的二维list
        # 初始化
        val = coins[0]
        for j in range(amount+1):
            ret[0][j] = int(j / val) if j % val == 0 else -1
        # 递推
        for i in range(1, m):
            for j in range(amount+1):
                if j-coins[i] >= 0 and ret[i][j-coins[i]] > -1:
                    a = ret[i][j-coins[i]]+1
                else:
                    a = -1
                b = ret[i-1][j]
                if a == -1 and b == -1:
                    ret[i][j] = -1
                elif a == -1:
                    ret[i][j] = b
                elif b == -1:
                    ret[i][j] = a
                else:
                    ret[i][j] = min(a, b)
        
        return ret[m-1][amount]

                
# @lc code=end

# Accepted
# 188/188 cases passed (1820 ms)
# Your runtime beats 8.95 % of python3 submissions
# Your memory usage beats 12.2 % of python3 submissions (19.4 MB)
