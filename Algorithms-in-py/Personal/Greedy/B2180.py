import sys
input = sys.stdin.readline
n = int(input())
func = []
zero = []
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        zero.append((a, b))
    else:
        func.append((a, b))

func.sort(key=lambda x : x[1]/x[0])
func = func + zero
t = 0
for item in func:
    t = (t + (item[0]*t)%40000 + item[1])%40000

print(t)