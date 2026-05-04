def solution(arr, start, end):
    answer = 0
    while start < end:
        if arr[start] == arr[end]:
            start += 1
            end -= 1
            continue
        answer += 1  # 수정하기
        if arr[start] < arr[end]:
            arr[start + 1] = arr[start] + arr[start + 1]
            start += 1
        else:
            arr[end - 1] = arr[end] + arr[end - 1]
            end -= 1

    return answer


n = int(input())

arr = list(map(int, input().split()))

# arr = []
# for i in range(n):
# 	arr.append(int(input()))

start = int(0);
end = int(n - 1);

print(solution(arr, start, end))
