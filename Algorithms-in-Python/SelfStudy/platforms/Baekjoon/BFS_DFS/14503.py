import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
    
# 0 빈칸, 1 벽, -1 청소됨

# 북, 동, 남, 서
dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]
answer = 0

def dfs(r, c, d):
    global answer
    # 청소 되지 않은 경우 청소
    if room[r][c] == 0:
        room[r][c] = -1 # 청소함
        answer += 1
    
    # 청소되지 않은 빈칸 찾기
    for _ in range(4):
        d = (d + 3) % 4 # 반시계 90도 회전
        new_r = r+dir_x[d]
        new_c = c+dir_y[d]
        if 0 <= new_r < n and 0 <= new_c < m and room[new_r][new_c] == 0: # 청소안한 빈칸
            dfs(new_r, new_c, d)
            return # 다시 1번부터

    # 4 방향 없으면 후진
    new_r = r-dir_x[d]
    new_c = c-dir_y[d]
    if not ((0 <= new_r < n) and (0 <= new_c < m)) or room[new_r][new_c] == 1: 
        return
    dfs(new_r, new_c, d)    

dfs(r, c, d)

print(answer)

# for i in range(n):
#     print(room[i])