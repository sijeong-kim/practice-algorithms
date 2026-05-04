import copy

#입력
n=int(input())
array=[]
for _ in range(n):
    array.append(list(map(int, input().split())))

#dp table
d=copy.deepcopy(array) #깊은 복사

#dp 전개
for i in range(1, n):
    for j in range(len(array[i])):
        if j==0:
            left=0
        else:
            left=d[i-1][j-1]
        if j==len(array[i])-1:
            right=0
        else:
            right=d[i-1][j]
        d[i][j]=max(left, right)+array[i][j]
#최대값
ans=0
for i in range(5):
    ans=max(ans, d[n-1][i])
#출력
print(ans)

#dp table에 데이터를 저장하면 공간복잡도가 준다.
#max함수는 리스트는 그냥 인수로 사용 가능
#len()을 쓰는 것보다는 변수로 나타내는 것이 더 시간복잡도가 좋다.
