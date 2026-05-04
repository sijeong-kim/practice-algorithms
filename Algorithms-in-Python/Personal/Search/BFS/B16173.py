import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

space = []
for i in range(n):
    space.append(list(map(int, input().split())))


dx = [1, 0]
dy = [0, 1]


isReachable = False

queue = deque()


queue.append((0, 0, space[0][0]))
while queue:
    x, y, cost = queue.popleft()
    print("x, y, cost:", x, y, cost)

    if cost == -1:
        isReachable = True
        break

    q = deque()
    q.append((x, y, 0))

    while q:
        a, b, c = q.popleft()
        if c == cost:
            print("a, b, c, space[a][b]:", a, b, c, space[a][b])
            queue.append((a, b, space[a][b]))
            continue

        for i in range(2):
            na = a + dx[i]
            nb = b + dy[i]
            if na<0 or na>n-1 or nb<0 or nb>n-1:
                continue
            # if c+1 == cost:
            #     print("a, b, na, nb, c, cost", a, b, na, nb, c, cost)
            #     queue.append((na, nb, space[na][nb]))
            #     continue
            q.append((na, nb, c+1))
    
if isReachable:
    print("HaruHaru")
else:
    print("Hing")