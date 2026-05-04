# 다시 풀기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [(b[i], i) for i in range(m)]
c.sort(key = lambda x : (-x[0], x[1]))

total = 24*n
score = sum(a)

remain = []
for b_value, idx in c:
    t = (100 - a[idx]) // b_value
    if (total < t):
        score += total * b_value
        break
    total -= t
    score += t * b_value

print(score)

# m개의 과목
# t시간 공부 -> a + t*b
# 총 공부 시간: 24 * n

