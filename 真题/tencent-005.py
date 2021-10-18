from math import sqrt

def solution():
    n = int(input())
    w = [int(_) for _ in input().split()]
    father = [int(_) for _ in input().split()]
    count = 0
    idx = n
    while idx > 1:
        tmp = w.pop()
        idx -= 1
        f_idx = father[idx - 1] - 1
        num = w[f_idx]
        if isSquare(num*tmp): count += 1
        while f_idx > 0:
            f_idx = father[f_idx - 1] - 1
            num = w[f_idx]
            if isSquare(num*tmp): count += 1

    print(count)

def isSquare(num):
    if sqrt(num) % 1 == 0:
        return True
    return False


solution()