# BOJ 18310

# 입력
n = int(input())
array = list(map(int, input().split()))
array.sort() # 정렬

print(array[(n-1)//2]) # 중간값 위치의 집 위치 출력
