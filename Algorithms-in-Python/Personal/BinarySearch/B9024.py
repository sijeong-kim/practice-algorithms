import sys
input = sys.stdin.readline

t = int(input())

while t > 0:
    t -= 1

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)

    ans = 0
    closeNum = int(1e9)
    closeCnt = 0
    low = 0
    high = n-1

    while low < high:
        tem = arr[low] + arr[high]
        if tem == k:
            # print("arr[low], arr[high]", arr[low], arr[high])
            low+=1
            high-=1
            ans+=1
        elif tem > k:
            if abs(closeNum - k) > abs(tem - k):
                closeNum = tem
                closeCnt = 1
            elif abs(closeNum - k) == abs(tem - k):
                closeCnt += 1
            high -= 1
        else:
            if abs(closeNum - k) > abs(tem - k):
                closeNum = tem
                closeCnt = 1
            elif abs(closeNum - k) == abs(tem - k):
                closeCnt += 1
            low += 1

    if ans != 0:
        print(ans)
    else:
        print(closeCnt)
