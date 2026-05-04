import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
# sys.setrecursionlimit(10**6)

cache = [100001]*100001

ans = 100001
queue = deque()
queue.append((n, 0))

while queue:
    x, t = queue.popleft()
    if t >= ans:
        continue
    if x == k:
        ans = min(t, ans)

    nx1 = x-1
    nx2 = x+1
    nx3 = 2*x

    # if nx1 == k or nx2 == k or nx3 == k:
    #     # print("x, nx1, nx2, nx3, t:", x, nx1, nx2, nx3, t)
    #     ans = min(t+1, ans)

    if 0 <= nx3 <= 100000 and cache[nx3] > t+1:
        cache[nx3] = t+1
        queue.append((nx3, t+1))
    if 0 <= nx2 <= 100000 and cache[nx2] > t+1:
        cache[nx2] = t+1
        queue.append((nx2, t+1))
    if 0 <= nx1 <= 100000 and cache[nx1] > t+1:
        cache[nx1] = t+1
        queue.append((nx1, t+1))

print(ans)
