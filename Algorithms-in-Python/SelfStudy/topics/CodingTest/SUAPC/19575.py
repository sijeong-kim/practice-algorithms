# import time
# start = time.time()
import sys
input = sys.stdin.readline
n, x = map(int, input().split())
poly = []
for i in range(n+1):
    a, t = map(int, input().split())
    poly.append(a)

k = int(1e9+7)
# print(poly)
ans = poly[0]

for i in range(1, n+1):
    # print(ans)
    ans = (x * ans + poly[i])%k

print(ans%k)
# end = time.time()

# print(f"{end-start:.5f} sec")