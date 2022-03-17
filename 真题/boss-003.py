m = [1,2,2,6]
n = [3,4,5]
k = 6

def findMinK(m, n, k):
    l1 = len(m)
    l2 = len(n)
    l = l1 + l2
    if k == 1: return min(m[0], n[0])
    p1 = 0
    p2 = 0
    for _ in range(1, k):
        if p1 == l1-1: return n[k-l1-1]
        if p2 == l2-1: return m[k-l2-1]
        if m[p1] <= n[p2]: p1 += 1
        else: p2 += 1
    return min(m[p1], n[p2])


if __name__ == "__main__":
    print(findMinK(m, n, k))
# 不对