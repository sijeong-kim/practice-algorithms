# 수정 필요 아직 틀림...


import sys
input = sys.stdin.readline
from collections import deque



dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
ans = [[-1]*m for _ in range(n)]

queue = deque()

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:

            ans[i][j] = 0
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>n-1 or ny<0 or ny>m-1:
            continue
        if graph[nx][ny] == 0:
            ans[nx][ny] = 0
            continue
        # if graph[nx][ny] < graph[x][y]:
        #     continue
        if graph[nx][ny] == 1 and ans[nx][ny] == -1:
            ans[nx][ny] = ans[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()