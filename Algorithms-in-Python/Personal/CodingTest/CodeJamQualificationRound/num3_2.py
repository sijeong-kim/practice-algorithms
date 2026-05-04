import sys
input = sys.stdin.readline
                      
def solution():
    s = [0] * (n+1)
    s[1] = dices[1]
    cnt = 1
    
    for i in range(2, n+1):
        if dices[i] == s[i-1]:
            s[i] = dices[i]
            if i - s[i] < 1:
                cnt += 1
        else:
            s[i] = s[i-1] + 1
            cnt += 1

    return cnt
    
if __name__ == "__main__":
    
    t = int(input())
    for i in range(t):
        n = int(input())
        dices = [0] + list(map(int, input().split()))
        dices.sort()
        
        ans = solution()
        print(f"Case #{i + 1}:", ans)
