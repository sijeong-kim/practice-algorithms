import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        now_val, now = heapq.heappop(q)
        if now_val > dist[now]:
            continue
        for next in graph[now]:
            cost = now_val + next[1]
            if cost < dist[next[0]]:
                dist[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


dijkstra(start)

print(dist[end])
