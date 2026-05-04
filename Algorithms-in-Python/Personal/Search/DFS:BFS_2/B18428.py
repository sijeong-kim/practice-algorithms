import sys
input=sys.stdin.readline

from itertools import combinations

n=int(input())

# 선생님 위치 저장 리스트
teachers=[]
# 장애물 놓을 수 있는 빈 공간 저장 리스트
spaces=[]
# 복도 정보 저장 리스트
data=[]

for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j]=='T':
            teachers.append((i, j))
        if data[i][j]=='X':
            spaces.append((i, j))

# 네 방향에 학생이 있는지 확인하는 함수
def check(x, y):
    for i in range(x+1, n):
        if data[i][y]=='O':
            break
        if data[i][y]=='S':
            return True
    for i in range(x-1, -1, -1):
        if data[i][y]=='O':
            break
        if data[i][y]=='S':
            return True
    for i in range(y+1, n):
        if data[x][i]=='O':
            break
        if data[x][i]=='S':
            return True
    for i in range(y-1, -1, -1):
        if data[x][i]=='O':
            break
        if data[x][i]=='S':
            return True
    return False
    
# 한 명이라도 감지하는지 확인하는 함수
def process():
    for x, y in teachers:
        # 네 방향에 학생이 있는지 확인
        if check(x, y)==True:
            return True
    return False

ok=False # 가능한지 확인하는 변수
for case in combinations(spaces, 3):
    for x, y in case:
        data[x][y]='O'
    # 감시를 피한 경우
    if process()==False:
        ok=True
        break
    for x, y in case:
        data[x][y]='X'

if ok==True:
    print('YES')
else:
    print('NO')
