n, m = map(int, input().split())
x, y, direction = map(int, input().split())
x = m - x - 1

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 시작지점 표시
result = 1
graph[y][x] = 2

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

stop = 0
while True:
    # 네 방향 모두 바다거나 가본 칸이라면
    if stop == 4:
        # 반대 방향으로 이동
        back = (direction + 2) % 4
        nx = x + dx[back]
        ny = y + dy[back]
        # 갈수 없는 경우 움직임을 멈춘다.
        if nx<0 or nx>=m or ny>=n or ny<0 or graph[ny][nx] == 1:
            break
        x, y = nx, ny
        stop = 0
        continue
    # 왼쪽 방향으로 회전 후 이동
    direction = (direction + 1) % 4
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 0:
        result += 1
        graph[ny][nx] = 2 # 가본 칸 2로 표시
        x, y = nx, ny
        stop = 0
        continue
    stop += 1

print(result)