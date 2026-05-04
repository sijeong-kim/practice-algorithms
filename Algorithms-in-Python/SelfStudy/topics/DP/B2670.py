import sys
input = sys.stdin.readline
n = int(input())

dp = []
for i in range(n):
    dp.append(float(input()))

for i in range(1, n):
    if dp[i-1] * dp[i] > dp[i]:
        dp[i] = dp[i-1] * dp[i]

ans = max(dp)
print("{:.3f}".format(ans))
