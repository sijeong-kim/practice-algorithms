import sys

input=sys.stdin.readline # 시간 초과 방지

n, m=map(int, input().split())

# 정보 담은 그래프
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

# 울타리 설치 후, 바이러스 전파할 그래프
temp = [[0]*m for _ in range(n)]

# 4가지 방향에 대한 그래프
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스 전파 함수 - DFS
def virus(x, y):
    if temp[x][y]==1:
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m: # 범위에 포함된다면
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

# 안전 영역 개수 계산 함수
def cnt_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score
                
# 울타리 세 개 설치 - DFS
result=0
def dfs(count):
    global result # 전역 변수 result
    # 울타리 세 개 설치 후 확인
    if count==3:
        # temp에 울타리 세 개 설치한 그래프 정보 저장
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i, j)
        # 안전 영역 개수 계산
        result = max(cnt_score(), result)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1
                dfs(count)
                graph[i][j]=0
                count-=1
dfs(0)
print(result)

