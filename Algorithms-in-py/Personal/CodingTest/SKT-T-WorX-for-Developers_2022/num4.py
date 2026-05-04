from collections import deque

def solution(grid, k):
    m = len(grid[0])
    n = len(grid)
    result = m * n

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append((0, 0, 0, 0))

    while q:
        x, y, move, count = q.popleft()
        # visited[x][y] = True

        if x == n-1 and y == m-1: # 도착
            if result > count:
                result = count
                continue
                
        if move >= k and grid[x][y] == 'F': continue # 숲

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
            if grid[nx][ny] == '#': continue # 강
            # if visited[nx][ny]: continue
            if move == k:
                q.append((nx, ny, 0, count+1))
            elif move < k:
                q.append((nx, ny, 0, count+1))
                q.append((nx, ny, move+1, count))

    return result
