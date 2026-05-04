n, m=map(int, input().split())
array=list(map(int, input().split()))

start=0
end=max(array)

result=0
while start<=end:
    mid=(start+end)//2
    total=0
    for length in array:
        if length>mid:
            total += length-mid
    if total<m:
        end=mid-1
    else: #total>=m
        start=mid+1
        result=mid #적어도 m만큼 가져가는 높이의 최대값

print(result)

#파라메트릭 서치

