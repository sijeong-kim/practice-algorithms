import sys
input = sys.stdin.readline

def solution(m, n, puddles):

    dp = [[0]*m for _ in range(n)]

    for p in puddles:
        dp[p[1]-1][p[0]-1] = -1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] = 0
            elif i==0 and j==0:
                dp[i][j] = 1
            elif i==0:
                dp[i][j] = dp[i][j-1]
            elif j==0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    

    return dp[n-1][m-1] % 1000000007
