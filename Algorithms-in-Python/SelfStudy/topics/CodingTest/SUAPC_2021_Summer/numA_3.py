import sys
input = sys.stdin.readline

import math

N, K = map(int, input().split())
people = list(map(int, input().split()))

people.sort()
v_possible = []

for k in range(1, N):
    tmp = people[0] * k + people[k] * (N-k)
    v_possible.append(tmp)

ans = math.ceil(K/max(v_possible))
print(ans)