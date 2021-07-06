#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        l = len(s)
        result = list()
        flag = 1
        sign_set = 0
        for i in range(l):
            c = s[i]
            if c == ' ' and not sign_set:
                continue
            elif c in ['+', '-']:
                if sign_set:
                    break
                else:
                    flag = 0 if c == '-' else 1
                    sign_set = 1
            elif '0' <= c <= '9':
                sign_set = 1
                result.append(c)
            else:
                break
        result_num = 0
        result_l = len(result)
        for idx in range(result_l):
            result_num = int(result[idx]) + result_num * 10
        if not flag:
            result_num *= -1
        if result_num > 2**31-1:
            return 2**31-1
        elif result_num < -1 * (2**31):
            return -1 * (2**31)
        else:
            return result_num
# @lc code=end
