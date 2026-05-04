import sys
input = sys.stdin.readline

INF = 1e9
n = int(input())
m = int(input())

# 이차원 리스트
dist = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신은 0으로 초기화
for i in range(1, n + 1):
    dist[i][i] = 0

# 버스 정보 입력
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 가장 짧은 간선만 저장
    if cost < dist[a][b]:
        dist[a][b] = cost

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
