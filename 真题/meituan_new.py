n, m = [int(_) for _ in input().split()]
bombs = [int(_) for _ in input().split()]

f = [[0 for _ in range(n)] for _ in range(m)]
minimum = 0

# initialize
f[0][0] = 0
for j in range(1, n):
    f[0][j] = 1
f[0][bombs[0]-1] = 99999
for i in range(1, m):
    bomb = bombs[i] - 1
    for j in range(n):
        if j == bomb:
            f[i][bomb] = 99999
        elif f[i-1][j] == 99999:
            f[i][j] = minimum + 1
        else:
            f[i][j] = f[i-1][j]
    minimum = min(f[i])
    
print(minimum)