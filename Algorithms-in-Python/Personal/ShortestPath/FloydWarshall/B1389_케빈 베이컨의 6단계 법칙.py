# 가중치 1인 최단 거리 찾기 => 플로이드 워셜

import sys
input = sys.stdin.readline
INF = int(1e2)+1

n, m = map(int, input().split())

# 최단 거리
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] <= 1:
                continue
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = 0
minNum = INF
for i in range(1, n+1):
    # for j in range(1, n+1):
    #     print(graph[i][j], end=' ')
    # print()
    num = sum(graph[i]) - INF
    if minNum > num:
        minNum = num
        ans = i

print(ans)