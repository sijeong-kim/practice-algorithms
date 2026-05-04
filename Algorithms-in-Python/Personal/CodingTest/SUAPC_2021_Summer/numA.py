import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
velocity = list(map(int, input().split()))
velocity.sort()

ans = int(1e18)
for i in range(1, n):
    v1 = velocity[i]
    v2 = velocity[0]
    pN2 = i
    pN1 = n - i
    
    t1 = v1 * pN1
    t2 = v2 * pN2

    q1 = t1/(t1+t2)
    q2 = t2/(t1+t2)
    
    w1 = k * q1
    w2 = k * q2

    # print(w1, w2)
    # print(w1/t1, w2/t2)
    t = math.ceil(max(w1/t1, w2/t2))
    if t < ans:
        ans = t
    
print(ans)


