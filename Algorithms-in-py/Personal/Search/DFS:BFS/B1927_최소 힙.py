import sys
import heapq
input = sys.stdin.readline
q = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)
