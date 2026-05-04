#테스트 케이스 입력
for tc in range(int(input())):
    #입력
    n, m = map(int, input().split())
    array=list(map(int, input().split()))

    #dp table 초기화
    d=[]
    index=0
    for i in range(n):
        d.append(array[index:index+m])
        index+=m

    #dp 진행
    for j in range(1, m):
        for i in range(n):
            if i==0:
                d[i][j] = d[i][j]+max(d[i][j-1], d[i+1][j-1])
            elif i==n-1:
                d[i][j] = d[i][j]+max(d[i][j-1], d[i-1][j-1])
            else:
                d[i][j] = d[i][j]+max(d[i][j-1], d[i-1][j-1], d[i+1][j-1])
    result=0
    for i in range(n):
        result=max(result, d[i][m-1])
    print(result)
    
