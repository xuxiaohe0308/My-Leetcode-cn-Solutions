# 自己实现堆（最大堆）
class myHeap:
    def __init__(self, arr:list=[]):
        self.heapArr = arr
        self.length = len(arr)
        self.buildUpHeap()

    # 直接展示堆结构（数组表示完全二叉树）
    def __str__(self):
        return str(self.heapArr)

    def __len__(self):
        return self.length

    # 维护堆，假设根节点的两个子树均是最大堆
    def maxHeapify(self, root:int=0):
        if root >= self.length:
            return
        
        largest = root
        left = (root << 1) + 1
        right = (root << 1) + 2

        if left < self.length and self.heapArr[left] > self.heapArr[largest]:
            largest = left

        if right < self.length and self.heapArr[right] > self.heapArr[largest]:
            largest = right

        if largest != root:
            self.heapArr[root], self.heapArr[largest] = self.heapArr[largest], self.heapArr[root]
            self.maxHeapify(largest)

    # 整体规范成最大堆（自底向顶）
    def buildUpHeap(self):
        if self.length <= 1:
            return

        parent = (self.length - 2) >> 1

        while parent >= 0:  # 不是根节点
            self.maxHeapify(parent)
            parent -= 1

    # 输出堆排之后的数组
    def sorted(self):
        # 由于偷懒了，直接在原数组上修改了。为了方便这里将堆记录下来，输出完之后还原
        arr_temp = self.heapArr

        i = self.length - 1
        res = []
        while (i >= 0):
            self.heapArr[i], self.heapArr[0] = self.heapArr[0], self.heapArr[i]
            res.append(self.heapArr[i])
            i -= 1
            self.length -= 1
            self.heapArr = self.heapArr[:-1]

            self.maxHeapify(0)
        
        # 还原
        self.heapArr = arr_temp
        self.length = len(arr_temp)

        return res
            

if __name__ == "__main__":
    heapTest = myHeap([0,1,2,3,4,5,6,7,8,9])
    print(heapTest.sorted())