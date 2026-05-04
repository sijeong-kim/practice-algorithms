import sys
input = sys.stdin.readline
                      
def solution():
    for t in range(4):
        for i in range(n*(t//2), n*(t//2) + n):
            for j in range(n*(t%2), n*(t%2) + n):
                if board[i][j] == 'I':
                    cnt_I[t] += 1
    return abs(cnt_I[0] - cnt_I[3]) + abs(cnt_I[1] - cnt_I[2])

    
    

if __name__ == "__main__":
    t = int(input())
    cnt = 0
    while t > 0:
        t -= 1
        cnt += 1
        
        n = int(input())
        board = [list(input().strip()) for _ in range(2*n)]
        cnt_I = [0] * 4
        ans = solution()
        
        print(f"Case #{cnt}:", ans)
