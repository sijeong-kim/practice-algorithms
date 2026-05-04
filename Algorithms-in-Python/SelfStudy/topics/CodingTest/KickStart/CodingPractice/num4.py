
# 실패!
dj = [1, 0, -1, 0, -1, 1]
di = [0, 1, 0, 1, 1, -1]

status = ""

def dfs(type, i, j, board_size, board):
    global status
    
    if type == 'B':
        if j == board_size-1:
            status = "Blue wins"
            return
    else:
        if i == board_size-1:
            status = "Red wins"
            return
        
    if board[i][j] == type:

        for s in range(6):
            for t in range(6):
                ni = i+di[s]
                nj = j+dj[t]
                if 0 > ni or board_size <= ni or 0 > nj or board_size <= nj:
                    continue
                if type != board[ni][nj]:
                    continue
                dfs(type, ni, nj, board_size, board)
                
def game_status(board_size, board):
    # TODO: implement this method to determine the status of the game board
    global status
    
    status = ""
    
    # Blue wins
    tmp_board = board
    for i in range(board_size):
        if board[i][0] == 'B':
            dfs('B', i, 0, board_size, tmp_board)
    
    # Red wins
    tmp_board = board
    for j in range(board_size):
        if board[0][j] == 'R':
            dfs('R', 0, j, board_size, tmp_board)
    
    # Impossible
    b_cnt = 0
    r_cnt = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'B':
                b_cnt += 1
            elif board[i][j] == 'R':
                r_cnt += 1    
    
    if  abs(b_cnt - r_cnt) > 1:
        status = "Impossible"
    
    # Nobody wins
    if status == "":
        status = "Nobody wins"    
    
    return status

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
