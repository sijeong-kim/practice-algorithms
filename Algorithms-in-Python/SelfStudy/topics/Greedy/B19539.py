import sys

input = sys.stdin.readline
n = int(input())
height = list(map(int, input().split()))

a, b = 0, 0
for i in range(n):
    a += height[i] % 2
    b += height[i] // 2

if (b < a):
    print("NO")
elif (b == a):
    print("YES")
else:
    if ((b-a) % 3 == 0):
        print("YES")
    else:
        print("NO")