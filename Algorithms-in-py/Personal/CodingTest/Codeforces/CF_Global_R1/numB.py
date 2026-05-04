import sys
input = sys.stdin.readline

t = int(input())

while(t>0):
    t-=1
    l, r = map(int, input().split())
    
    for i in range(17, 0, -1):
        p = r // int(pow(2, i))
        if p == 1:
            idx = i
            break

    arr = [i for i in range(l, r+1)]
    ans = [0] * (idx+1)

    
    for i in range(idx, -1, -1):
        q = int(pow(2, i))

        for j in range(r-l+1):
            if arr[j] // q == 1:
                ans[i] += 1
                arr[j] %= q

    print((r-l+1)-max(ans))


