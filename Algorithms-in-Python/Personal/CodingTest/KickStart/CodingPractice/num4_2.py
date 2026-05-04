import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, 1, -1, 0, -1]

# 오른쪽에 파란색이 도달하면 true를 반환하는 함수
def checkBlue(idx, board_size, board):
    q = deque()
    q.append((idx, 0))
    
    while(q):
        x, y = q.popleft()
        if y == board_size-1:
            return True
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size:
                continue
            if board[nx][ny] == 'B':
                q.append((nx, ny))
    
    return False

# 아래쪽에 빨간색이 도달하면 true를 반환하는 함수    
def checkRed(idx, board_size, board):
    q = deque()
    q.append((0, idx))
    
    while(q):
        x, y = q.popleft()
        if y == board_size-1:
            return True
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size:
                continue
            if board[nx][ny] == 'R':
                q.append((nx, ny))

def game_status(board_size, board):
    # TODO: implement this method to determine the status of the game board
    ans = ""
    cnt_b = 0
    cnt_r = 0
    win = 0
    
    for i in range(board_size):
        for j in range(board_size):
                
            if board[i][j]=='B':
                cnt_b += 1
                if j==0:
                    if checkBlue(i, board_size, board):
                        ans = "Blue wins"
                        win += 1
                    
            elif board[i][j]=='R':
                cnt_r += 1
                if i==0:
                    if checkRed(j, board_size, board):
                        ans = "Red wins"
                        win += 1
    
    if abs(cnt_b - cnt_r) > 1 or win > 1: 
        ans = "Impossible"
    
    if ans == "":
        ans = "Nobody wins"
        
    return ans

def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        board_size = int(input())
        board = []
        for _ in range(board_size):
            board.append(list(input().strip()))

        ans = game_status(board_size, board)

        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
