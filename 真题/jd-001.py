def solution():
    (a, b, f, k) = [int(_) for _ in input().split()]
    rest = k  # 剩余次数
    tank = b  # 油箱还剩多少
    f1 = a - f
    charge_count = 0
    flag = 1  # 1右0左
    if b < max(f, f1): return -1

    while True:
        if flag:
            rest_dict = f1  # 剩余距离
            next_dict = f  # 到加油站距离
        else:
            rest_dict = f
            next_dict = f1
        if tank < next_dict: return -1

        tank -= next_dict
        if rest == 1:
            return charge_count if tank >= rest_dict else charge_count+1
        if tank < (2*rest_dict): 
            charge_count += 1
            tank = b

        tank -= rest_dict
        rest -= 1
        flag = 1 - flag

    return charge_count


print(solution())

