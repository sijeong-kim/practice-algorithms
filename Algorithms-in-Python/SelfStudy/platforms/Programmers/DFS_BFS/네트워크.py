def solution(n, computers):
    answer = 0
    # a, b, c 는 모두 같은 네트워크 상에 있음
    parents = [i for i in range(n)]
    
    
    def find_parent(x):

        while parents[x] != x: #루트에 도달 할 때까지 경로 압축
            parents[x] = parents[parents[x]]
            x = parents[x]
        return parents[x]

    def union(x, y):
        px = find_parent(x)
        py = find_parent(y)
        if px < py:
            parents[py] = px
        elif py < px:
            parents[px] = py


    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(i, j)
                
    # 정리
    
    return len(set(find_parent(i) for i in range(n)))

    # 네트워크 게수를 return