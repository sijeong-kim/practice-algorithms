import sys
input = sys.stdin.readline

move = [(1, 0), (0, 1), (1, 1)]

n, m = map(int, input().split())
candy = []
candy.append([0]*(m+1))
for i in range(n):
    candy.append([0]+list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        candy[i][j] = candy[i][j] + max(candy[i-1][j-1], candy[i-1][j], candy[i][j-1])

print(candy[n][m])
