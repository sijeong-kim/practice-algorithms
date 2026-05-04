import sys
input = sys.stdin.readline

def solution(m, n, puddles):

    dp = [[0]*m for _ in range(n)]

    for p in puddles:
        dp[p[1]-1][p[0]-1] = -1
    
    dp[0][0] = 1

    for i in range(1, n):
        if dp[i][0] == -1:
            dp[i][0] = 0
            continue
        dp[i][0] = dp[i-1][0]

    for i in range(1, m):
        if dp[0][i] == -1:
            dp[0][i] = 0
            continue
        dp[0][i] = dp[0][i-1]

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n-1][m-1] % 1000000007