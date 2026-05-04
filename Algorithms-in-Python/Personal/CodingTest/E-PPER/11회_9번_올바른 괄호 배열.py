# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

dp = [0] * (user_input+1)

dp[0] = 1
dp[1] = 1

# 카탈란 수
for i in range(2, user_input+1):
	for j in range(i):
		dp[i] += dp[j]*dp[i-j-1]

print(dp[user_input])