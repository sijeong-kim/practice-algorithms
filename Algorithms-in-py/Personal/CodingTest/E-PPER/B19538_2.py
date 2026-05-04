import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

graph = [[]]

for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input())

rumor = list(map(int, input().split()))
believe = [-1] * (n+1)
queue = deque()
for r in rumor:
    believe[r] = 0
    queue.append((r, 0))

while queue:
    now, time = queue.popleft()

    for u in graph[now]:
        if u == 0:
            break
        if believe[u] == -1: # 아직 루머 믿지 않는 사람
            
            # 주변인 반 이상 루머 믿는지 확인
            cnt = 0
            for v in graph[u]:
                if 0 <= believe[v] <= time: # 같은 시기에 갱신된 시간에 영향 받지 않기 위해 범위 설정
                    cnt += 1
            
            if cnt*2 >= len(graph[u])-1:
                believe[u] = time+1
                queue.append((u, time+1))

for i in range(1, n+1):
    print(believe[i], end=' ')

# 어려웠던 점: 같은 시기에 전파되는 것이 queue에서 차례대로 방문된다.
# 같은 시기에 전파되는 사람끼리 서로 영향 주지 않게 조건을 설정하는 것이 어려웠다.