import sys

input = sys.stdin.readline

t = int(input())
cnt = 0
while t > 0:
    t -= 1
    cnt +=1
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    
    ans = sum(c) % m
    print(f"Case #{cnt}:", ans)
    
