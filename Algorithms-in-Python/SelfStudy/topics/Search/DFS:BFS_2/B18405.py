from collections import deque
import sys
input=sys.stdin.readline

n, k = map(int, input().split())
# 바이러스 정보 리스트
data=[]

# 시험관 정보 그래프
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
    # 바이러스 위치 정보 저장
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j], 0, i, j)) # 튜플로 저장 # 시간도 저장

# 목표 시간, 좌표
target_s, target_x, target_y = map(int, input().split())

# 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# BFS
data.sort() # 오름 차순 증식
q = deque(data)

while q:
    num, s, x, y = q.popleft()
    if target_s == s: # 정확히 s초가 다 지났을 때
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=num
                q.append((num, s+1, nx, ny))
                
print(graph[target_x-1][target_y-1])
