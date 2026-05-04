import sys
input = sys.stdin.readline
from collections import deque


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

data = []
cache = [[0]*10 for _ in range(10)]

for i in range(10):
    tem = list(input().rstrip())
    for j in range(10):
        if tem[j] == 'L':
            lx, ly = i, j
    data.append(tem)
    
q = deque()
q.append((lx, ly))
# ans = 0

isFinished = False
while(q and not isFinished):
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 0 or nx > 9 or ny < 0 or ny > 9):
            continue
        if cache[nx][ny] != 0:
            continue
        if data[nx][ny] == 'R' or data[nx][ny] == 'L':
            continue
        if data[nx][ny] == '.':
            cache[nx][ny] = cache[x][y] + 1
            q.append((nx, ny))
        if data[nx][ny] == 'B':
            isFinished = True
            ans = cache[x][y]
            break

            
print(ans)
