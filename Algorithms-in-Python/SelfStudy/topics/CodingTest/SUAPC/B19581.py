import sys
input = sys.stdin.readline


n = int(input())
adj = [0]*(n+1)

tree =[[0]*(n+1) for i in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c
    adj[a] += 1
    adj[b] += 1

adjlist = []
for i in range(1, n+1):
    if adj[i] == 1:
        adjlist.append(i)

print(adjlist)
print(tree)
s = 0

if len(adjlist) == 2:
    # 단말 사이의 거리에서 가장 끝에 있는 것 중 작은 가중치 가장 작은 것 빼기
    start = adjlist[0]
    end = adjlist[1]

    next = start
    while next != end:
        for i in range(1, n+1):
            if tree[next][i] != 0:
                print("next, i", next, i)
                if next == start:
                    l = tree[next][i]
                if i == end:
                    r = tree[next][i]
                s += tree[next][i]
                next = i
    if l > r:
        s -= r
    else:
        s -= l

# else:
#     # 단말인 것 사이 거리 중 두번째인 것

print(s)