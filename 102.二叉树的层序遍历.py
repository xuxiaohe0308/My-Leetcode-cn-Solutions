#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 两个队列，一个存旧的一个存新的
        result = []
        nodeQueue = queue.Queue()
        # 第一个节点入队
        if root:
            nodeQueue.put(root)
        while not nodeQueue.empty():
            temp = []
            newQueue = queue.Queue()
            while not nodeQueue.empty():
                node = nodeQueue.get()
                temp.append(node.val)
                if node.left:
                    newQueue.put(node.left)
                if node.right:
                    newQueue.put(node.right)
            result.append(temp)
            nodeQueue = newQueue
        return result
        
# @lc code=end

# Accepted
# 34/34 cases passed (48 ms)
# Your runtime beats 12.4 % of python3 submissions
# Your memory usage beats 11.63 % of python3 submissions (15.5 MB)