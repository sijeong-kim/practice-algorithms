#입력
a=input()
b=input()
n=len(a)
m=len(b)

#dp table
d=[[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][0]=i
for j in range(1, m+1):
    d[0][j]=j
#dp 전개
for i in range(1, n+1):
    for j in range(1, m+1):
        #문자가 같은 경우
        if a[i-1]==b[j-1]:
            d[i][j]=d[i-1][j-1]
        #문자가 다른 경우
        else:#삽입, 삭제, 교체 중 최소
            d[i][j]=min(d[i][j-1], d[i-1][j], d[i-1][j-1])+1

#출력
print(d[n][m])
