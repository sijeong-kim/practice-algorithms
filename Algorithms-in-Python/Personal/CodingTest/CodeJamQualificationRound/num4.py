import sys
from itertools import permutations
input = sys.stdin.readline

def trigger(start, visited):
    
    fun_val = 0
    while True:
        visited[start] = True
        fun_val = max(fun_val, factors[start])
        
        start = points[start] - 1
        if start == -1 or visited[start]:
            break
        
    return fun_val
               
def solution():
    in_degree = [0] * n
    
    for i in range(n):
        if points[i]:
            in_degree[points[i]-1] += 1
    
    starts = []
    for i in range(n):
        if in_degree[i] == 0:
            starts.append(i)
    
    max_val = 0
    for case in permutations(starts):
        
        visited = [False] * n
        sum_fun = 0
        for start in case:
            sum_fun += trigger(start, visited)
        max_val = max(sum_fun, max_val)
    
    return max_val
    
if __name__ == "__main__":

    t = int(input())
    
    for i in range(t):
        n = int(input())
        
        factors = list(map(int, input().split()))
        points = list(map(int, input().split()))
        
        ans = solution()
        print(f"Case #{i + 1}:", ans)
