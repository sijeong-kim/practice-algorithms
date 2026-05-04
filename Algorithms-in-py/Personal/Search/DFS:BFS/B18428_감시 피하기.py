n=int(input()) # 복도의 크기
board = [] # 복도 정보(N * N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j]=='T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j]=='X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction==0:
        while y>=0:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            y-=1
    # 오른쪽 방향으로 감시
    if direction==1:
        while y<n:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            y+=1
    # 위쪽 방향으로 감시
    if direction==2:
        while x>=0:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            x-=1
    if direction==3:
        while x<n:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            x+=1
    return False

# 장애물 설치 후에 한 명이라도 학생이 감지되는지 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
        return False

find=False
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y]='O'
    if not process():
        find=True
        break
    for x, y in data:
        board[x][y]='X'

if find:
    print('YES')
else:
    print('NO')
    
