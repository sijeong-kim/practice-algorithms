# 다시 풀기!!!

from collections import deque 
import sys
input = sys.stdin.readline

n = int(input())
believeRumor = [0] + [-1]*n
neighbors = [[]]
for i in range(n):
    neighbors.append(list(map(int, input().split())))
m = int(input())
firstRumor = list(map(int, input().split()))

queue = deque()
for fr in firstRumor:
    queue.append((fr, 0))
    believeRumor[fr] = 0

while queue:
    num, min = queue.popleft()

    spread = []
    # 주변인 절반 이상이 루머를 믿으면 루머 믿음 -> spread에 추가
    for next in neighbors[num]:
        if next == 0:
            break
        if believeRumor[next] != -1:
            continue
        
        count = 0
        for nb in neighbors[next]:
            if nb == 0:
                break
            if believeRumor[nb] != -1:
                count += 1
        
        half = len(neighbors[next])//2
        if half <= count:
            spread.append(next)

    # 루머 처음 믿기 시작하는 시간 갱신
    for s in spread:
        believeRumor[s] = min+1
        queue.append((s, min+1))

for i in range(1, n+1):
    print(believeRumor[i], end=" ")