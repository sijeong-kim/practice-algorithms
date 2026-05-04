import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
num = list(map(int, input().split()))

for i in range(m):
    low = 0
    high = n-1
    ans = 0
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] < num[i]:
            low = mid+1
        elif arr[mid] > num[i]:
            high = mid-1
        else:
            ans = 1
            break
    print(ans)