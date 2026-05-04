import queue  # FIFO 큐 구현

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 사과의 위치
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1  # 사과 있음 1

# 뱀의 방향 변환 정보
turn_num = int(input())

turn_time = []
for _ in range(turn_num):
    t, d = input().split()
    turn_time.append((int(t), d))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀이 존재하는 칸 저장하는 큐
q = queue.Queue()
q.put((1, 1))

# 시작
head_x, head_y = 1, 1
graph[head_x][head_y] = 2  # 뱀 있음 2
direction = 0  # 오른쪽 이동
time = 0  # 시간


def turn_left():
    global direction
    direction = (direction - 1) % 4


def turn_right():
    global direction
    direction = (direction + 1) % 4


while True:
    # 방향 바꾸기
    for turn in turn_time:
        if turn[0] == time:
            if turn[1] == 'L':
                turn_left()
            else:
                turn_right()
    # 이동할 죄표 계산
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]
    time += 1
    if 0 >= nx or nx > n or 0 >= ny or ny > n:  # 벽이라면 끝
        break
    elif graph[nx][ny] == 2:  # 뱀의 몸이라면 끝
        break
    elif graph[nx][ny] == 1:  # 사과 있다면 몸 그대로
        pass
    else:  # 사과가 없다면
        tail_x, tail_y = q.get()
        graph[tail_x][tail_y] = 0  # 꼬리가 있는 칸 비워준다.
    # 머리 이동
    graph[nx][ny] = 2
    head_x, head_y = nx, ny
    q.put((nx, ny))

print(time)
