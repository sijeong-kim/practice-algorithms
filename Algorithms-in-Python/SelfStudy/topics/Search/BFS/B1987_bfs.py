import time
start = time.time()
####################

import sys
input = sys.stdin.readline
from collections import deque

alpha = []
r, c = map(int, input().split())
for i in range(r):
    alpha.append(list(input()))
cache = [['']*c for _ in range(r)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
queue = deque()
queue.append((0, 0, alpha[0][0]))
ans = 1

while queue:
    x, y, v = queue.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if cache[nx][ny] == v + alpha[nx][ny]:
                continue
            if alpha[nx][ny] in v:
                continue
            else:
                cache[nx][ny] = v + alpha[nx][ny]
                queue.append((nx, ny, v + alpha[nx][ny]))
                ans = max(len(v)+1, ans)

print(ans)

# visited를 False로 만드는 부분이 뭘까?
# 메모리초과: 큐의 크기가 제한되어 있기 때문에, 각 위치에서 중복된 문자열 체크해서 큐에 넣었어야 함 -> cache 배열

end = time.time()

print(f"{end-start:.5f} sec")