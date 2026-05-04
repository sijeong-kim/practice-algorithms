# 틀림!!
import sys
input = sys.stdin.readline 

def union(a, b):
    idx = len(edges) - 1
    for i in range(1, idx):
        x, y = edges[i]
        print(x, y)
        if a < x < b or a < y < b or x < a < y or x < b < y:
            u = find(i)
            v = find(idx)
            if u < v:
                parent[u] = v
        print(parent)

def find(a):
    while parent[a] != a:
        a = parent[a]
    return parent[a]

def judge(a, b):
    if find(a) == find(b):
        print(1)
    else:
        print(0)

n = int(input())

parent = [0]
edges = [0]
for i in range(n):
    t, a, b = map(int, input().split())
    if t == 1:
        parent.append(len(parent))
        edges.append((a, b))
        union(a, b)

    else:
        judge(a, b)






