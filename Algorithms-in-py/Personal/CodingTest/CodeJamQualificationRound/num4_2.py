import sys
input = sys.stdin.readline

def cal_max(s):
    r_max_val = 0
    while True:
        r_max_val = max(factors[s], r_max_val)
        if len(in_degree[s]) == 1:
            s = in_degree[s][0]
        elif len(in_degree[s]) == 0:
            return r_max_val
        else: break
    
    max_val= 0
    min_val = int(1e9)
    for m in in_degree[s]:
        tmp = cal_max(m)
        max_val += tmp
        if min_val > tmp:
            min_val = tmp
    max_val -= min_val
    max_val += max(min_val, r_max_val)    
        
    return max_val

def solution():
    ans = 0
    for s in starts:
        ans += cal_max(s)
    return ans
    
if __name__ == "__main__":

    t = int(input())
    
    for j in range(t):
        n = int(input())
        
        factors = list(map(int, input().split()))
        points = list(map(lambda x: int(x)-1, input().split()))
        
        in_degree = [[] for i in range(n)]
        starts = []
        for i in range(n):
            if points[i] != -1:
                in_degree[points[i]].append(i)
            else:
                starts.append(i)
        
        ans = solution()
        print(f"Case #{j + 1}:", ans)
