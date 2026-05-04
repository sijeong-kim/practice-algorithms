import sys
input = sys.stdin.readline


n, x = map(int, input().split())

c = list(map(int, input().split()))
c.sort(reverse=True)

checked = [False]*n

count = 0

for i in range(n):
    if checked[i]:
        continue
    checked[i] = True
    if c[i] == x:
        count += 1
        continue
    # if c[i] >= x/2:
    #     for j in range(n-1, i, -1):
    #         if not checked[j]:
    #             checked[j] = True
    #             count += 1
    #             break
    #     continue
    if c[i] >= x/4:
        for j in range(n-1, i, -1):
            if not checked[j]:
                if c[i] + c[j] >= x/2:
                    checked[j] = True
                    count += 1
                    break
        continue
    break

count += checked.count(False)//4
print(count)