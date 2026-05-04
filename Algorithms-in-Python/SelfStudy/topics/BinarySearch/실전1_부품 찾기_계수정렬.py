n=int(input())
a=[0]*1000001

for i in input().split():
    a[int(i)]=1;
    
m=int(input())
b=list(map(int, input().split()))
for i in b:
    if a[i]==1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
