import sys
input = sys.stdin.readline

chess = []
n, m = map(int, input().split())
for i in range(n):
    chess.append(list(input().split()))

graph = [[0]*n for i in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        for u in range(4):
            nx = i + dx[u]
            ny = j + dy[u]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            if chess[nx][ny] == chess[i][j]:
                graph[i][j] += 1



        



