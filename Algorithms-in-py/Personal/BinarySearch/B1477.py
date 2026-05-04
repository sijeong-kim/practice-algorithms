import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
pos = [0] + list(map(int, input().split())) + [l]

pos.sort()
dist=[(pos[i+1]-pos[i]) for i in range(n+1)]

# print("pos: ", pos) # [0, 82, 201, 411, 555, 622, 755, 800]
# print("dist: ", dist) # [82, 119, 210, 144, 67, 133, 45]
high = max(dist)
low = 0

# count + mid -
# mid: 휴게소가 앖는 구간의 최대값
mVal = 1001

while low <= high:
    mid = (low + high) // 2

    count = 0
    for u in dist:
        count += ((u-1) // mid)

    # print("mid:", mid, "count:", count)
    if count <= m: 
        if mVal > mid:
            mVal = mid
        high = mid - 1 # mid - count +
    else:
        low = mid + 1
    
print(mVal)
