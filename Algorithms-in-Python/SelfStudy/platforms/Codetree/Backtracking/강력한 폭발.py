n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


# 격자를 직접 칠했다가 지우는 방식 X
# 폭탄 선택 조합을 완성한 뒤 별로 visited 초토와 칸 수 세기


# 폭탄 위치를 먼저 따로 저장
# DFS로 각 위치마다 3가지 폭탄 모두 시도



# 폭탄 위치 DFS 전에 미리 저장
bomb_pos = [] 

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_pos.append((i, j))

# 폭탄 위치 저장
bombs = [
    [(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0)], # 1번 폭탄
    [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)], # 2번 폭탄
    [(0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 3번 폭탄
]

# grid 직접 수정 하지 말고 visited 카운트 배열 사용
visited = [[0] * n for _ in range(n)]

# 가장 많은 폭탄수 (답)
answer = 0

# grid 범위 안인지 확인하는 함수 (True/False)
def in_range(x, y):
    return 0<=x<n and 0<=y<n


def put_bomb(x, y, bomb_type):
    
    added = [] # 이번에 놓은 폭탄 어디에 놓았는지 저장
    count = 0 # 이번에 놓은 폭탄 총 몇개 놓게 되었는지 저장

    for dx, dy in bombs[bomb_type]:
        nx = x + dx
        ny = y + dy

        if not in_range(nx, ny):
            continue
        
        # 방문 X 폭탄 놓기
        if visited[nx][ny] == 0:
            count += 1
        # 방문 표시
        visited[nx][ny] += 1
        added.append((nx, ny))

    return count, added # 저장한 후 사용


def remove_bomb(added):

    # 방문 없앰
    for x, y in added:
        visited[x][y] -= 1



def dfs(idx, total): # 백트래킹 idx: 폭탄 인덱스, total: 지금까지 놓인 폭탄 개수
    global answer # 최종 답 최대 폭탄 개수

    # 폭탄 개수 만큼 다 확인 한 경우
    if idx == len(bomb_pos): # 모든 폭탄 위치에 폭탄 설치
        answer = max(answer, total) # total 이 answer 보다 큰지 확인
        return # 종료

    x, y = bomb_pos[idx]

    for bomb_type in range(3):
        count, added = put_bomb(x, y, bomb_type) # 이번에 놓은 폭탄 수, 이번에 놓은 폭탄 위치
        dfs(idx + 1, total + count) # 다음 인덱스로 dfs
        remove_bomb(added) # 이번에 놓은 폭탄 위치 없애기




dfs(0, 0)
print(answer)