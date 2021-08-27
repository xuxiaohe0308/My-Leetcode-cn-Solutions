#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    t = stack.pop() 
                    if (char == ')' and t != '(') or (char == ']' and t != '[') or (char == '}' and t != '{'):
                        return False
        if len(stack) > 0:
            return False
        return True
                
# @lc code=end
