import math
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def func(n, r, c):
    
    if n==1:
        return 2*r+c
    
    # 큰 사각형에서 r, c 위치 0, 1 로 나타내기
    if c == 0:
        pc = 0
    else:
        pc = int(math.log2(c))
    if r == 0:
        pr = 0
    else:
        pr = int(math.log2(r))

    # 작은 사각형 개수
    square = 2 * (pr//(n-1)) + (pc//(n-1))
    
    # 작은 사각형 한변 길이
    width = int(math.pow(2, (n-1)))

    # 작은 사각형에서 위치
    c %= width
    r %= width

    return func(n-1, r, c) + square * int(math.pow(width, 2))

print(func(n, r, c))

# 어려웠던 부분: ValueError로 런타임에러
# 1. 파이썬에서 연산자 쓸 때 괄호 주의
# 2. 파이썬 제곱 math.pow 함수
# 3. a<1; log(a) < 0 인 걸 잊고 있었다!!
# int 함수는 음수를 처리하지 못함!! 10진수 정수 문자열, 실수형을 값으로 받음