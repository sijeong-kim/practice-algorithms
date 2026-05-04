from math import *
import sys

input = sys.stdin.readline

def solution1():
    
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    pairs = []
    for i in range(n):
        pairs.append((i, b.index(a[i])))
    
    print(pairs)
    
    cnt = 0
    for a, b in pairs:
        for i in range(n):
            if (pairs[i][0]-a) * (pairs[i][1]-b) < 0:
                cnt += 1
    print(cnt//2)

# 구간합 쿼리
def cnt_visited(node, start, end, left, right):
    
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    
    
def solution2():
    
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dicB = {}
    for i, num in enumerate(b):
        dicB[num] = i
    
    # segment tree
    h=int(ceil(log2(n)))
    t_size = 1 << (h+1)
    
    tree = [0] * t_size

    ans = 0
    for i in range(n):
        ans += cnt_visited(1, 0, n-1, dicB[a[i]], n-1)
        
    print(ans)
  
if __name__ == "__main__":
    solution2()

