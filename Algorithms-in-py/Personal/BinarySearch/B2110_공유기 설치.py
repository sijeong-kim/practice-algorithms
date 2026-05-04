# BOJ 2110

#입력
n, c=map(int, input().split())

array=[]
for _ in range(n):
    array.append(int(input()))

array.sort() # 정렬

# 이진 탐색
start=1
end=array[-1]-array[0]

result=0
while start<=end:
    mid=(start+end)//2
    value=array[0]
    count=1
    # 공유기 설치
    for i in range(1, n):
        if array[i]>=value+mid:
            value=array[i]
            count+=1
    if count>=c: # 거리 증가
        start=mid+1
        result=mid #최적값 저장
    else: # count<c일 때, 거리 감소
        end=mid-1

print(result)
