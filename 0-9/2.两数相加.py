#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        result = temp
        while True:
            temp = listNodeAdd(temp, l1, l2)
            if (not l1.next) and (not l2.next):
                break
            if not l1.next:
                l1.next = ListNode()
            if not l2.next:
                l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next
            if not temp.next:
                temp.next = ListNode()
            temp = temp.next
        return result

def listNodeAdd(ln, n1, n2):
    temp = n1.val + n2.val
    if temp < 10:
        ln.val += temp
        if ln.val == 10:
            ln.val = 0
            ln.next = ListNode()
            ln.next.val = 1
    else:
        ln.next = ListNode()
        ln.val += (temp - 10)
        ln.next.val = 1
    return ln

# @lc code=end

