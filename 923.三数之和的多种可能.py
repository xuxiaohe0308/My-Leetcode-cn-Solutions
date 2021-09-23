#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 三数之和的多种可能
#

# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        l = len(arr)
        arr.sort()
        h = 3
        mat = [[[0 for _ in range(h)] for _ in range(target+1)] for _ in range(l)]

        for j in range(target+1):
            if j == arr[0]:
                mat[0][j][0] = 1
        for i in range(1, l):
            for j in range(target+1):
                mat[i][j][0] = mat[i-1][j][0]+1 if j == arr[i] else mat[i-1][j][0]
                for k in range(1, h):
                    if j-arr[i] >= 0:
                        mat[i][j][k] = (mat[i-1][j][k] + mat[i-1][j-arr[i]][k-1]) % (1e9+7)
                    else:
                        mat[i][j][k] = mat[i-1][j][k]
        return int(mat[l-1][target][h-1])
# @lc code=end

# Accepted
# 71/71 cases passed (3296 ms)
# Your runtime beats 18.42 % of python3 submissions
# Your memory usage beats 5.26 % of python3 submissions (101 MB)

