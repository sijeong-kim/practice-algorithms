import sys
input = sys.stdin.readline

n = int(input())


info = []
for i in range(n):
    d, c = map(int, input().split())
    info.append((d, c))

cnt = 0
for i in range(n):
    isCandi = True
    nd, nc = info[i]

    for j in range(n):
        if i==j:
            continue
        if nd > info[j][0] and nc >= info[j][1]:
            isCandi=False
        if nc > info[j][1] and nd >= info[j][0]:
            isCandi=False
            
    if isCandi:
        cnt += 1
if n==1:
    print(1)
else:
    print(cnt)