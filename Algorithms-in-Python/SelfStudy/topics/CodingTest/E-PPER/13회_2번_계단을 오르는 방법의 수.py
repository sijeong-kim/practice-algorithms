# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input("계단의 수를 입력하시오 : "))

# dp
ways = [0]*(n+1)
ways[1] = 1
ways[2] = 2

for i in range(3, n+1):
	ways[i] = ways[i-1] + ways[i-2]

ans = ways[n]
print("계단 오르는 방법의 수 : " + str(ans))