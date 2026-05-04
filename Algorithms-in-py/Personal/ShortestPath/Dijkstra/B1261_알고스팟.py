INF = int(1e4)+1

import heapq

m, n = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 데이터 리스트에 미로 정보 저장
data = []
for _ in range(n):
    data.append(list(map(int, input())))

# 각 방에서 부순 벽 최소 개수 저장
graph = [[INF]*m for _ in range(n)]


# 다익스트라 알고리즘 함수
def dijkstra(start_x, start_y):
    q = []
    heapq.heappush(q, (0, start_x, start_y))
    graph[start_x][start_y] = 0
    while q:
        # 현재 노드 pop
        nowVal, nowX, nowY = heapq.heappop(q)
        # 이미 처리한 정보라면 continue
        if nowVal < graph[nowX][nowY]:
            continue
        for i in range(4): # 상하좌우로 이동
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if(0 <= nx < n) and (0 <= ny < m):
                # nextVal 구하기
                if data[nx][ny] == 1:
                    nextVal = graph[nowX][nowY] + 1
                else:
                    nextVal = graph[nowX][nowY]
                # 만약 기존 부순 벽 개수보다 작으면, 값 갱신 & 큐에 push
                if nextVal < graph[nx][ny]:
                    graph[nx][ny] = nextVal
                    heapq.heappush(q, (nextVal, nx, ny))

dijkstra(0, 0)

print(graph[n-1][m-1])

