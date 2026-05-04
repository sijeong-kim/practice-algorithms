import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # graph = [[0]*(n+1) for _ in range(n+1)]
    # adj = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        # graph[a][b] = 1
        # graph[b][a] = 1
        # adj[a] += 1
        # adj[b] += 1
    print(n-1)
    



