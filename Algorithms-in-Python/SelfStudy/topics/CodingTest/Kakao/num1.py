def solution(id_list, report, k):
    
    n = len(id_list)

    arr = [[0] * n for i in range(n)]
    messaged = [0] * n

    for r in report:
        r1, r2 = r.split(' ')
        p1 = id_list.index(r1)
        p2 = id_list.index(r2)
        arr[p2][p1] = 1

    for i in range(n):
        if sum(arr[i]) >= k:
            for j in range(n):
                if arr[i][j] != 0:
                    messaged[j] += 1
    
    return messaged


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k= 2
print(solution(id_list, report, k))