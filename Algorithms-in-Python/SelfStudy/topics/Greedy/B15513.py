import sys
input = sys.stdin.readline

n = int(input())
lottery = []
for i in range(n):
    w, q = map(int, input().split())
    lottery.append((w, q, i+1))

lottery.sort(key=lambda x: -(x[0]/(10000-x[1])))

for i in lottery:
    print(i[2], end=' ')
