def solution(p):
    n = len(p)
    answer = [0] * n
    for i in range(n-1):
        j = p.index(min(p[i:]))
        if i != j:
            p[i], p[j] = p[j], p[i] 
            answer[i] += 1
            answer[j] += 1
    return answer
