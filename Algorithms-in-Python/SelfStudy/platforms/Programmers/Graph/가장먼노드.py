# import heapq
from collections import deque
def solution(n, vertex):
    
    graph = [[] for _ in range(n+1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
        
    INF = int(1e9)
    distances = [INF] * (n+1)
    
    q = deque([(1, 0)])
    # q = [(1, 0)]
    
    
    distances[1] = 0
    
    while q:
        v, dist = q.popleft()
        
        for nv in graph[v]:
            if distances[nv] > dist + 1:
                distances[nv] = dist + 1
                q.append((nv, dist + 1))
                
    max_val = -1
    cnt = 0
    for dist in distances:
        if dist != INF:
            if max_val < dist:
                max_val = dist
                cnt = 1
            elif max_val == dist:
                cnt += 1
            
    return cnt
    # return sum(1 for dist in distances if dist == max_val)
         
    
    
    
    