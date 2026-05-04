import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())

n = int(input())
cubes = [0] * 20

for i in range(n):
    a, b = map(int, input().split())
    cubes[a] = b

before = 0
ans = 0
for i in range(n-1, -1, -1):
    before <<= 3

    possibleCube = (length >> i) * (width >> i) * (height >> i) - before
    newCube = min(cubes[i], possibleCube)
    before += newCube
    ans += newCube

if before == length * width * height:
    print(ans)
else:
    print(-1)
