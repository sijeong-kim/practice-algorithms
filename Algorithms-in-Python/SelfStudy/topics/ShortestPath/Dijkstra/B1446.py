import sys
input = sys.stdin.readline

n, d = map(int, input().split())

shortcut = [[] for _ in range(10001)]

for i in range(n):
    s, e, w = map(int, input().split())
    shortcut[s].append([w, e])

distance = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0:  # 이전 지점에서 고속도로로 도착하는 경우
        distance[i] = min(distance[i], distance[i-1]+1)
    for w, e in shortcut[i]:
        if e <= d and distance[e] > w + distance[i]: # 시작 지점이 i인 지름길
            distance[e] = w + distance[i]

print(distance[d])