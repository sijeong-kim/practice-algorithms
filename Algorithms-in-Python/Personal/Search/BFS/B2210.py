import sys
input = sys.stdin.readline
from collections import deque

graph = []
for _ in range(5):
    graph.append(list(input().split()))

string = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy, graph[sx][sy]))
    # cache = [['']*5 for _ in range(5)]
    # print("x, y, s:", sx, sy, graph[sx][sy])
    while queue:
        x, y, s = queue.popleft()
        # print("x, y, s:", x, y, s)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>4 or ny<0 or ny>4:
                continue
            if s+graph[nx][ny] in string:
                continue
            # if cache[nx][ny] == s+graph[nx][ny]:
                # continue
            if len(s) < 5:
                # cache[nx][ny] = s+graph[nx][ny]
                queue.append((nx, ny, s+graph[nx][ny]))
                continue
            string.append(s+graph[nx][ny])

for i in range(5):
    for j in range(5):
        bfs(i, j)
    
# print(string)
print(len(string))