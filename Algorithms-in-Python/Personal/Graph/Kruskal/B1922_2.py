# import time
# start = time.time()

# 최소 스패닝 트리 - Kruskal 알고리즘

import sys
input = sys.stdin.readline

# union-find 함수
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    i = find(i)
    j = find(j)
    if i > j:
        parent[j] = i
    else:
        parent[i] = j

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
edges = []

# 간성 정보 입력받기
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 작은 비용의 경로부터 체크하면서 다른 집합이면 같은 집합으로 만들기
edges.sort()


cost = 0

for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        cost += c

print(cost)

# end = time.time()
# print(f"{end-start:.5f} sec")