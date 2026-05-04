#정수 n, m 입력받기
n, m = map(int, input().split())

#n개의 화폐 단위 정보를 입력받기
array=[]
for i in range(n):
    array.append(int(input()))
array.sort()

#최소한의 화폐 개수 DP table 초기화
#10001은 특정 금액 만들 수 있는 화폐 구성이 존재하지 않는다는 의미
d=[10001]*(m+1)

#DP 진행(보텀업)
d[0]=0
for k in array:
    for i in range(k, m+1):
        if d[i-k]!=10001: #(i-k)원을 만드는 화폐 구성이 존재하는 경우
            d[i]=min(d[i], d[i-k]+1)

#출력
if d[m]==10001: #최종적으로 m원을 만드는 화폐 구성이 존재하지 않는 경우
    print(-1)
else:
    print(d[m])
