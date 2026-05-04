# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 프로그래머스에서는 main함수 및 입출력문이 필요하지 않습니다. 대신 solution함수만 작성하면 됩니다.
# def solution(필요한 인자들) :
def solution(user_input):
    #  필요한변수/제어코드

    answer = ""
    if user_input[0] == '1':
        answer += '1'

    idx = 0
    count = 0
    for i in range(len(user_input)):
        start = user_input[idx]
        if start != user_input[i]:
            answer += chr(ord('A') + count - 1)  # 아스키 코드, 숫자 변환 함수
            # 초기화
            count = 0
            idx = i

        count += 1

    answer += chr(ord('A') + count - 1)

    #  return  변수
    return answer


user_input = input()

print(solution(user_input))

