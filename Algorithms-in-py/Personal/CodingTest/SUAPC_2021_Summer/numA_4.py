import sys
input = sys.stdin.readline

import math

N, K = map(int, input().split())
people = list(map(int, input().split()))

people.sort()
tmp = 0
for k in range(1, N):
    tmp = max(people[0]*k + people[k]*(N-k), tmp)
ans = math.ceil(K / tmp)

print(ans)