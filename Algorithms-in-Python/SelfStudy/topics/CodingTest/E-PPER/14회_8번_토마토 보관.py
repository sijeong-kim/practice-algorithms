# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 실제 시험에서는 solution 함수를 사용한다는 점을 감안하고 풀이해주세요.
from collections import deque
queue = deque()

m, n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

flag = False
ans = 0
for i in range(n):
    if flag:
        break
    for j in range(m):
        if graph[i][j] == 0:
            ans = 0
            flag = True
            break
        if graph[i][j] > ans:
            ans = graph[i][j]

print(ans - 1)


