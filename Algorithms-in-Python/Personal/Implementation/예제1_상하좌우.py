n = int(input())
moves = input().split()

# 이동 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x, y = 1, 1

for move in moves:
    # 이동 계획에 따라 좌표 계산
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 정사각형 공간 벗어나는 움직임 무시
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    # 아니면, 이동 수행
    x, y = nx, ny

print(x, y)
