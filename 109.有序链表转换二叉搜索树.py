#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None: return None
        if head.next == None: return TreeNode(head.val)
        slow, fast = head, head
        temp = head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            temp = slow
            slow = slow.next
        mid = slow
        root = TreeNode(mid.val)
        temp.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

# @lc code=end

# Accepted
# 32/32 cases passed (60 ms)
# Your runtime beats 85.84 % of python3 submissions
# Your memory usage beats 82.82 % of python3 submissions (18.3 MB)
