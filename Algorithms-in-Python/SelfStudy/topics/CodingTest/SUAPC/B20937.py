import sys
input = sys.stdin.readline

n = int(input())
dishes = list(map(int, input().split()))

dishes.sort()
dishes.append(0)

cnt = 1
i = 0
while i < n:
    if dishes[i] == dishes[i+1]:
        # print("i",i)
        for j in range(i+1, n+1):
            # print("j",j)
            if dishes[i] != dishes[j]:
                cnt = max(j-i, cnt)
                i = j
                break
    i += 1

print(cnt)