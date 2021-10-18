# cut rope
def solution():
    n_nums = int(input())
    l = [int(_) for _ in input().split()]
    l.sort()
    p1, p2 = 0, 0
    max = 0
    n = l[0]
    while p2 < n_nums:
        count = 0
        t = l[p2]
        while p2 < n_nums and l[p2] == t:
            p2 += 1
            count += 1
        n = l[p2-1]
        while l[p1] < n/2:
            p1 += 1
        tmp = n_nums + count - p1
        if tmp > max: max = tmp

    print(max)

solution()