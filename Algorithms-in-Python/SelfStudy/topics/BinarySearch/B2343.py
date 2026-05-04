n, m = map(int, input().split())
lessons = list(map(int, input().split()))

# m개의 블루레이에 모든 기타 레슨 동영상을 녹화
# 불루레이 개수(count) 최대 m개일 때, 블루레이 크기(mid) 최소

low = max(lessons)
high = sum(lessons)

ans = high

# mid: 블루레이 크기
# count: 가능한 블루레이 최소 개수 (최대한 욱여넣음)

while low <= high:
    mid = (low + high) // 2

    count = 0
    t = 0
    for u in lessons:
        t += u
        if t > mid:
            count += 1
            t = u
    count += 1

    # print("mid:", mid, "low:", low, "high:", high, "count:", count, "ans:", ans)
    # print("mid:", mid, "count:", count, "ans:", ans)
    # mid + count -
    # mid 최소 count 최대
    if count <= m:
        high = mid - 1 # mid -
        if ans > mid:
            ans = mid
    else:
        low = mid + 1 # mid +

print(ans) 
    