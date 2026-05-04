n=int(input())
t=[0]*n #상담 기간
p=[0]*n #상담 금액
d=[0]*(n+1) #dp table
max_value=0

for i in range(n):
    t[i], p[i] = map(int, input().split())

for i in range(n-1, -1, -1):
    time = t[i]+i
    
    if time <= n:
        d[i] = max(p[i]+d[time], max_value)
        max_value=d[i]
    else:
        d[i]=max_value
print(max_value)
        
