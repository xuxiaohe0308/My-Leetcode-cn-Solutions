#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class ListNode:

    def __init__(self, k=0, val=0, left=None, right=None):
        self.k = k
        self.val = val
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.count = 0
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            temp = self.dict[key]
            # update location
            self._updateLoc(temp)
            return temp.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            # update
            temp = self.dict[key]
            temp.key = key
            temp.val = value
            self._updateLoc(temp)
            return

        if self.count == self.capacity:
            # drop tail
            self._dropTail()
        # add head
        self._addHead(key, value)


    def _dropTail(self):
        temp = self.tail
        if self.tail.left is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.left
            self.tail.right = None
        self.count -= 1
        self.dict.pop(temp.k)
        del(temp)

    def _updateLoc(self, temp: ListNode):
        # drop middle
        if temp.left is None:
            return 
        if temp.right is None:
            temp.left.right = None
            self.tail = temp.left
        else:
            temp.left.right, temp.right.left = temp.right, temp.left
        # add to head
        temp.left = None
        temp.right = self.head
        self.head.left = temp
        self.head = temp
        

    def _addHead(self, key, value):
        temp = ListNode(key, value)
        if self.count == 0:
            self.head = temp
            self.tail = temp
        else:
            self.head.left = temp
            temp.right = self.head
            self.head = temp
        self.dict[key] = temp
        self.count += 1
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end

# Accepted
# 22/22 cases passed (588 ms)
# Your runtime beats 69.71 % of python3 submissions
# Your memory usage beats 9.65 % of python3 submissions (71.7 MB)