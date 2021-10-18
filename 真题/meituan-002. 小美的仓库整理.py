n_goods = int(input())
weights = [int(n) for n in input().split()]
order = [int(n) for n in input().split()]
maximum = 0
nums = [0,] * (n_goods+2)
result = [0, ]
for i in range(n_goods-1):
    idx = order[n_goods-i-1]
    num = weights[idx-1]
    temp = num
    # 向后扩散
    i = idx + 1
    while nums[i] > 0:
        temp += nums[i]
        i += 1
    # 向前扩散
    i = idx - 1
    while nums[i] > 0:
        temp += nums[i]
        i -= 1
    
    nums[idx] = num
    if temp > maximum:
        result.append(temp)
        maximum = temp
    else:
        result.append(maximum)

for i in range(n_goods):
    print(result[n_goods-i-1])