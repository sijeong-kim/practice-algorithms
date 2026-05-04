"""
https://www.acmicpc.net/workbook/view/1983
DFS+BFS 필수 문제
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    

for i in range(n+1):
    graph[i].sort()


def dfs(now, graph, visited):
    if visited[now]: return
    visited[now] = True
    print(now, end=" ")
    for next in graph[now]:
        dfs(next, graph, visited)
        
def bfs(start, graph, visited):
    
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if visited[now]: continue
        visited[now] = True
        print(now, end=" ")
        
        
        for next in graph[now]:
            if visited[next]: continue
            q.append(next)

                
                
            
visited = [False] * (n+1)
dfs(v, graph, visited)
print()

visited = [False] * (n+1)
bfs(v, graph, visited)
print()