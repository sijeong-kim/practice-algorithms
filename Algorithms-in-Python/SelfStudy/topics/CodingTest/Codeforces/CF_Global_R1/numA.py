import sys
input = sys.stdin.readline

t = int(input())
while (t>0):
    t -= 1
    n = int(input())
    height = list(map(int, input().split()))
    
    r = sum(height) % n
    if r != 0:
        print(1)
    else:
        print(0)








    