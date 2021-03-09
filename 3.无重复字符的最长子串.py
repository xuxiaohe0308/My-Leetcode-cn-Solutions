#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        idx1 = 0
        idx2 = 0
        max_length = 0
        c_list = list()
        while idx1 < l:
            # 寻找idx1开始的最大子串
            while idx2 < l:
                c = s[idx2]
                if c in c_list:
                    break
                else:
                    c_list.append(c)
                idx2 += 1
            if idx2 - idx1 > max_length:
                max_length = idx2 - idx1
            idx1 += 1
            c_list = c_list[1:]
        return max_length
# @lc code=end
