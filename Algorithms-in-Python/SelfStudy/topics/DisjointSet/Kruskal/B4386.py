import sys, itertools, math
input = sys.stdin.readline

n = int(input())

parents = [i for i in range(n)]
coord = []
edges = []

def find(x):
    while parents[x] != x:
        x = parents[x]
    return x
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y: x, y = y, x
    parents[x] = y

for i in range(n):
    x, y = map(float, input().split())
    coord.append((x, y))

for s, e in itertools.combinations(parents, 2):
    d = math.sqrt(math.pow(coord[s][0] - coord[e][0], 2) + math.pow(coord[s][1] - coord[e][1], 2))
    edges.append((d, s, e))

edges.sort()

result = 0
for edge in edges:
    d, s, e = edge
    if find(s) != find(e):
        union(s, e)
        result += d

print(result)