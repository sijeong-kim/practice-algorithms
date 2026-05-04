import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
# n개의 도시
# 기름통의 크기 무제한
# 1km마다 1리터의 기름 사용
# 도시마다 리터당 가격 다름, 원 단위
# 도로의 길이 다름, km 단위

lengths = list(map(int, input().split()))    # 도로의 길이: 0, 1, ..., n-2
costs = list(map(int, input().split()))      # 리터당 가격: 0, 1, ..., n-2, n-1

result = 0

mVal = int(1e9) + 1
for i in range(n-1):
    if costs[i] < mVal:
        mVal = costs[i]
    result += mVal * lengths[i]

print(result)