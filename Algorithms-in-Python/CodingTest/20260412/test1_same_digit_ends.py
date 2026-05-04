def solution(A):
    largest_number = {}  # (first digit, last digit): 가장 큰 숫자 저장
    answer = -1 # 같은 경우가 없는 경우

    for x in A:
        # x의 첫 번째와 마지막 숫자 구하기
        last_digit = x % 10

        first_digit = x
        while first_digit >= 10:
            first_digit //= 10

        # (first_digit, last_digit)를 key로 사용
        key = (first_digit, last_digit)

        # key가 이미 존재하면
        if key in largest_number:
            # 현재 key에 대한 최대값과 현재 값의 합을 계산하여 answer 업데이트
            answer = max(answer, largest_number[key] + x)
            # 현재 값이 더 크면 largest_number[key] 업데이트
            if x > largest_number[key]:
                largest_number[key] = x
        # key가 존재하지 않으면 largest_number에 추가
        else:
            largest_number[key] = x

    return answer
