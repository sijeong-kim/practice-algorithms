import sys, math
input = sys.stdin.readline

n = int(input()) # 시험장 수
a = list(map(int, input().split())) # 응시자 수
b, c = map(int, input().split()) # 감시 가능 수

# 총 감독관
result = n

for i in range(n):
    a[i] -= b
    if a[i] <= 0:
        continue
    # 부 감독관
    result += math.ceil(a[i]/c)

print(result)
