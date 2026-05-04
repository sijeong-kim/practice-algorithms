import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

min_result=1e9
max_result=-1e9

def dfs(idx, now): # dfs의 매개변수: 현재 고정된 값(다른 단계에선 변하지만)
    global min_result, max_result, add, sub, mul, div
    if idx==n:
        min_result=min(min_result, now)
        max_result=max(max_result, now)
    else:
        if add>0:
            add-=1
            dfs(idx+1, now+data[idx])
            add+=1
        if sub>0:
            sub-=1
            dfs(idx+1, now-data[idx])
            sub+=1
        if mul>0:
            mul-=1
            dfs(idx+1, now*data[idx])
            mul+=1
        if div>0:
            div-=1
            dfs(idx+1, int(now/data[idx]))
            div+=1

dfs(1, data[0])
print(max_result)
print(min_result)
