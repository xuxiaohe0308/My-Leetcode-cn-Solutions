#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1
            x *= -1
        idx = 9
        num_list = []
        while idx >= 0:
            temp = x % (10**idx)
            if temp == x:
                if len(num_list) > 0:
                    num_list.append(0)
                idx -= 1
                continue
            else:
                num = x // (10**idx)
                num_list.append(num)
                x -= (num * (10**idx))
            idx -= 1
        length = len(num_list)
        if length == 0:
            return 0
        result = 0
        for idx in range(length):
            result += num_list[idx] * (10**idx)
        if flag:
            result *= -1
        if result > 2**31-1 or result < -1 * 2**31:
            return 0
        return result
# @lc code=end
