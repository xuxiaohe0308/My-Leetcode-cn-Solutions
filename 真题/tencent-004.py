def solution():
    n_input = int(input())
    mat_1 = [[-1 for _ in range(400)] for _ in range(400)]
    mat_2 = [[-1 for _ in range(400)] for _ in range(400)]
    mat_3 = [[-1 for _ in range(400)] for _ in range(400)]

    # 一开始先打三个表
    # 只有表名（mat_1, mat_2, mat_3）和i, j for循环的东西不一样
    # 马
    mat_1[0][0] = 0
    layer = 1
    queue = set()
    queue.add((0, 0))
    while len(queue):
        tmp = set()
        while len(queue):
            x, y = queue.pop()
            for i, j in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
                if in_bound(x+i, y+j) and (x+i, y+j) not in queue and mat_1[x+i][y+j] == -1:
                    mat_1[x+i][y+j] = layer
                    tmp.add((x+i, y+j))
        queue = tmp
        layer += 1

    # 象
    mat_2[0][0] = 0
    layer = 1
    queue = set()
    queue.add((0, 0))
    while len(queue):
        tmp = set()
        while len(queue):
            x, y = queue.pop()
            for i, j in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                if in_bound(x+i, y+j) and (x+i, y+j) not in queue and mat_2[x+i][y+j] == -1:
                    mat_2[x+i][y+j] = layer
                    tmp.add((x+i, y+j))
        queue = tmp
        layer += 1

    # 马+象
    mat_3[0][0] = 0
    layer = 1
    queue = set()
    queue.add((0, 0))
    while len(queue):
        tmp = set()
        while len(queue):
            x, y = queue.pop()
            for i, j in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -2), (-2, 2), (2, -2), (2, 2)]:
                if in_bound(x+i, y+j) and (x+i, y+j) not in queue and mat_3[x+i][y+j] == -1:
                    mat_3[x+i][y+j] = layer
                    tmp.add((x+i, y+j))
        queue = tmp
        layer += 1

    for _ in range(n_input):
        t, x, y = [int(_) for _ in input().split()]
        if t == 1:
            print(mat_1[x-1][y-1])
        elif t == 2:
            print(mat_2[x-1][y-1])
        else:
            print(mat_3[x-1][y-1])


def in_bound(x, y):
    if x >= 0 and x < 400 and y >= 0 and y < 400:
        return True
    return False

solution()
