import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
velocity = list(map(int, input().split()))
velocity.sort()

v1 = velocity[n//2]
v2 = velocity[0]
pN2 = n//2
pN1 = n - (n//2)

t1 = v1 * pN1
t2 = v2 * pN2
ans = math.ceil(k / (t1+t2))    
print(ans)