import sys
input = sys.stdin.readline

kimbab = []
n, k, m = map(int, input().split())
for i in range(n):
    l = int(input())
    if l <= k:
        continue
    elif l < 2 * k:
        l -= k
    else:
        l -= 2 * k
    # l = 2*k일때 0되는데 괜찮은가?
    kimbab.append(l)

low = 1
if kimbab:
    high = max(kimbab)
else:
    high = 1
    
mVal = -1
while low <= high:
    mid = (low + high) // 2
    
    count = 0
    for u in kimbab:
        count += u//mid
    # print("mid(p):", mid, "count:", count)

    if count >= m:
        if mVal < mid:
            mVal = mid
        low = mid + 1
    else:
        high = mid - 1

print(mVal)

