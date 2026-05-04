n = int(input())

person = list(map(int, input().split()))
results = [-1]*n # 결과

# 작은 키의 사람 부터 차례대로
# 공백을 왼쪽 키 큰 사람의 수만큼 비워두고 자리를 채운다.
for i in range(n):
    count = 0
    for j in range(n):
        if count == person[i] and results[j] == -1:
            results[j] = i+1
            break
        if results[j] == -1:
            count += 1


for result in results:
    print(result, end=' ')