import sys
from collections import deque

input = sys.stdin.readline # 시간 초과 방지

n, m, k, x = map(int, input().split())

# 거리 정보 인접 리스트로 구현
graph=[[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 정보 저장 리스트
distance=[-1]*(n+1)
distance[x]=0

# 너비 우선 탐색(BFS)
q=deque([x])

while q:
    now=q.popleft()
    for i in graph[now]: # 인접 노드
        if distance[i]==-1: # 아직 방문 하지 않는 노드
            q.append(i)
            distance[i]=distance[now]+1

exist=False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        exist=True
        
if not exist:
    print(-1)
