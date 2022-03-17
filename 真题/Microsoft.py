def solution(S):
    if len(S) <= 1: return 0
    blocks = []
    max = 0
    count = 1
    last = S[0]
    for c in S[1:]:
        if c == last: count += 1
        else:
            last = c
            blocks.append(count)
            if count > max: max = count
            count = 1
    blocks.append(count)
    if count > max: max = count
    result = 0
    for i in blocks:
        result += (max - i)
    return result

print(solution(input()))