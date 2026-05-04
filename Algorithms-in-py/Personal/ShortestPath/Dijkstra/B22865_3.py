# 시간초과 문제
# 모든 점 -> 세 점에 대해 다익스트라 알고리즘 적용
# 인접 행렬를 인접 리스트로 자료구조 변경헤서 탐색의 시간복잡도 감소
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
a, b, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    d, e, w = map(int, input().split())
    graph[e].append((w, d))
    graph[d].append((w, e))

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
        for w, i in graph[now]:
            cost = dist + w
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    ans.append(distance)
    # print(distance)

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