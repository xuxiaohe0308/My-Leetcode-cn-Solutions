def solution(N):
    N += 1
    s = list(str(N))
    l = len(s)
    if l <= 1: return int(s) 
    suffix = {0: '', 1: '0', 2: '01', 3: '010', 4: '0101', 5: '01010', 6: '010101', 7: '0101010', 8: '01010101', 9: '010101010'}
    for i in range(1, l):
        if s[i] == s[i-1]:
            if s[i] == '9':
                if i == 1: return int('1' + suffix[l])
                s[i-2] = str(int(s[i-2])+1)
                s[i-1:] = suffix[l-i+1]
            else:
                s[i] = str(int(s[i])+1)
                s[i+1:] = suffix[l-i-1]
            break

    return int(''.join(s))

print(solution(int(input())))