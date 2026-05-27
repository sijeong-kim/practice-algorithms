def solution(n, candy):
    count = 0

    target = sum(candy) // n
    for c in candy:
        if target - c > 0:
            count += target - c

    return count

T = int(input()) # 테스트 개수

for t in range(1, T+1):
    n = int(input()) # 상자 개수
    candy = list(map(int, input().split())) # n개 사탕 개수


    answer = solution(n, candy)
    print(f"#{t} {answer}")