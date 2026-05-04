from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input())
p = list(map(float, input().split()))

prob = 0



queue = deque()
queue.append(('0', 0, 1-p[0]))
queue.append(('1', 1, p[0]))
while queue:
    num, count, cost = queue.popleft()
    if len(num) == N-1:
        prob += count * cost
        continue
    if num[len(num)-1] == '0':
        queue.append((num+'1', count+1+1, cost * p[len(num)]))
        queue.append((num+'0', count, cost * (1-p[len(num)])))
    else:
        queue.append((num+'1', count+1, cost * p[len(num)]))
        queue.append((num+'0', count+1, cost * (1-p[len(num)])))

print(prob)