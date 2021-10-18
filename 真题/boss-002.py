def solution():
    s = input()
    l = len(s)
    a, b = 1, 1
    for _ in range(l-1):
        a, b = b, a + b
    print(b)

solution()
