n = int(input())
array = list(map(int, input().split()))

# dp table
# d[i]: array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
d = [1] * n

# dp 전개
# 가장 긴 증가하는 부분 수열 활용하기
for i in range(1, n):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + 1)

# 출력
print(n - max(d))
