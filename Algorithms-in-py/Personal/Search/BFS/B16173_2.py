# 틀림!!!


import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

space = []
for i in range(n):
    space.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

cache = [[False]*n for _ in range(n)]

isReachable = False
cache[0][0] = True
queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(2):
        nx = x + dx[i]*space[x][y]
        ny = y + dy[i]*space[x][y]
        if 0>nx or nx>n-1 or 0>ny or ny>n-1:
            continue
        if space[nx][ny] == -1:
            isReachable = True
            break
        if cache[nx][ny]:
            continue
        cache[nx][ny] = True
        queue.append((nx, ny))
    
if isReachable:
    print("HaruHaru")
else:
    print("Hing")
