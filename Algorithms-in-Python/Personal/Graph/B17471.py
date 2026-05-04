from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# bfs
def isConnected(l):
    visited = [False] * (n+1)
    queue = deque([])
    queue.append(l[0])
    visited[l[0]] = True

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if next in l and visited[next]==False:
                visited[next] = True
                queue.append(next)
    
    for u in l:
        if visited[u] == False:
            return False
    
    return True


n = int(input())

people = [0] + list(map(int, input().split()))
graph = [[]]

for i in range(1, n+1):
    l = list(map(int, input().split()))
    # count = l[0]
    graph.append(l[1:])

total = sum(people)
minVal = int(1e9)
flag = False

for i in range(1, n//2+1):
    cases = [k for k in range(1, n+1)]
    for j in combinations(cases, i):
        jc = list(set(cases) - set(j))
        # 연결 확인
        if isConnected(j) and isConnected(jc):
            flag = True
            s = 0
            for u in j:
                s += people[u]
            d = abs(total - 2 * s)
            if d < minVal:
                minVal = d

if flag:
    print(minVal)
else:
    print(-1)