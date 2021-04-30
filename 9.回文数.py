#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        string = list()
        idx = 0
        while True:
            string.append(x % 10)
            idx += 1
            x = x // 10
            if x == 0:
                break
        print(string)
        l = idx // 2
        if idx == 1:
            return True
        else:
            for i in range(l):
                if string[i] != string[idx-i-1]:
                    return False
            return True
# @lc code=end
