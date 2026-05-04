# 시간초과 문제
import time
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
a, b, c = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

m = int(input())
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d][e] = l
    graph[e][d] = l

start = time.time()

ans = []

def dijkstra(s):
    distance = [0] + [INF] * n
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in range(1, n+1):
            if graph[now][i]==0:
                continue
            cost = dist + graph[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    ans.append(distance)
    # print(val)

for s in [a, b, c]:
    dijkstra(s)

minV = -1
idx = -1
for i in range(1, n+1):
    t = min(ans[0][i], ans[1][i], ans[2][i])
    if minV < t:
        minV = t
        idx = i

print(idx)

end = time.time()

print(f"{end-start}:.5f sec")
