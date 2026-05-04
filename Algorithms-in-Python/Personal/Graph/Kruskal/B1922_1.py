import time
start = time.time()

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    
visited = [1]

cost = 0
while True:
    if len(visited) == n:
        break

    mVal = int(1e4)+1

    for v in visited:
        for j in range(1, n+1):
            if j not in visited:
                if graph[v][j] != 0:
                    if mVal > graph[v][j]:
                        mVal = graph[v][j]
                        mV = j

    cost += mVal
    visited.append(mV)

print(cost)

end = time.time()

print(f"{end-start:.5f} sec")