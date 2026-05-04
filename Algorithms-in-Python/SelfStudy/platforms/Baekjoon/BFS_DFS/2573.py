from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# N x M x V: 900,000

# bfs
def change(i, j, visited, melt):
    
    q = deque([(i, j)])
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()

        ocean = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < m): continue
            if array[nx][ny] == 0:
                ocean += 1
            elif not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
        
        melt[x][y] = ocean
        
answer = 0
end = False

while not end:
    
    visited = [[False] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    cnt = 0
    
    
    for i in range(n):
        if end: break
        for j in range(m): 
            if array[i][j] != 0 and not visited[i][j]:
                cnt += 1
                # 두 덩이인지 확인
                if cnt >= 2:
                    end = True
                    break
                # 녹음
                change(i, j, visited, melt)
                
    
    if cnt == 0: # 얼음 다 녹음
        break
    
    for i in range(n):
        for j in range(m):
            array[i][j] = max(0, array[i][j] - melt[i][j]) # 음수처리
    
    if not end:
        answer += 1

if end:
    print(answer)
else:
    print(0)