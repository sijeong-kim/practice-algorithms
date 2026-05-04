import time

start = time.time()
#############


import sys
input = sys.stdin.readline
r, c = map(int, input().split())
# sys.setrecursionlimit(10**6)

alpha = []
visited = [False] * 26
# vPos = [[False]*c for _ in range(r)]

for i in range(r):
    alpha.append(list(input()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[ord(alpha[nx][ny])-65]:
                visited[ord(alpha[nx][ny])-65] = True
                dfs(nx, ny, cnt+1)
                visited[ord(alpha[nx][ny])-65] = False
                
ans = 0
visited[ord(alpha[0][0])-65] = True
dfs(0, 0, 1)
print(ans)

# 시간 초과 남 -> 해결 못함

###############
end = time.time()

print(f"{end - start:.5f} sec")