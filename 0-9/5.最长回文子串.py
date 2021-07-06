#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        l = len(s)
        result = s[0]

        for idx in range(l):
            i = 0
            while True:  # 奇数回文
                if idx-i-1 < 0 or idx+i+1 >= l or s[idx-i-1] != s[idx+i+1]:
                    break
                else:
                    i += 1
            if 2 * i + 1 > max_length:
                max_length = 2 * i + 1
                result = s[idx-i: idx+i+1]
            i = 0
            while True:  # 偶数回文
                if idx-i-1 < 0 or idx+i >= l or s[idx-i-1] != s[idx+i]:
                    break
                else:
                    i += 1
            if 2 * i > max_length:
                max_length = 2 * i
                result = s[idx-i: idx+i]

        return result

# @lc code=end
