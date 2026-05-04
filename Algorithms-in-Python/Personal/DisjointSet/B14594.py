import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parents = [i for i in range(n)]

def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: 
        parents[b]=a
    else:
        parents[a]=b

cnt = 0
for i in range(m):
    x, y = map(int, input().split())
    x-=1
    y-=1
    for j in range(x, y):
        if find_parent(j) != find_parent(y):
            union(j, y)
            cnt += 1

print(n-cnt)