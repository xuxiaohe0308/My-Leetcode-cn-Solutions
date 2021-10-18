def solution():
    (n, k, x) = [int(_) for _ in input().split()]
    weight = [int(_) for _ in input().split()]
    weight.sort()
    length = len(weight)
    weight_delta = [0 for _ in range(len-1)]
    for i in range(len-1):
        weight_delta[i] = weight[i+1] - weight[i]
