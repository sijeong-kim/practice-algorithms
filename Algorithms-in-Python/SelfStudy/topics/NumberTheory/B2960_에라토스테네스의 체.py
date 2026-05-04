n, k = map(int, input().split())

arr = [True] * (n+5)

arr[0] = False
arr[1] = False
ans = 0
count = 0

# m = int(n ** 0.5)
# 제곱근까지 확인하는 이유는
# m과 n 사이의 소수가 아닌 수는 더 작은 값으로 모두 확인 하였기 때문
# 그런데 제곱근으로 풀면 틀렸다.
end = False
for i in range(2, n + 1):
    if end:
        break
    if arr[i]: # 소수
        # print(i)
        count += 1
        if count == k:
            ans = i
            break
        for j in range(i+i, n+1, i): # 소수의 배수는 소수 아님
            if arr[j]:
                # print(j)
                arr[j] = False
                count += 1
                if count == k:
                    ans = j
                    end = True
                    break

print(ans)

# 제곱근 반례
# 입력: 15 12
# 출력: 7
