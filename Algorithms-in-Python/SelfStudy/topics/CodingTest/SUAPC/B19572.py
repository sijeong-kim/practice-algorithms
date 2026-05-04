import sys
input = sys.stdin.readline

d1, d2, d3 = map(int, input().split())

sum = (d1 + d2 + d3)/2
c = round(sum-d1, 1)
b = round(sum-d2, 1)
a = round(sum-d3, 1)

ans = 1
if c<=0 or b<=0 or a<=0:
    ans = -1
    print(ans)
else:
    print(ans)
    print(a, b, c)