import sys
input = sys.stdin.readline
                      
def solution():
    s = [0] * (n+1)
    s[1] = dices[1]
    
    for i in range(2, n+1):
        if dices[i] == s[i-1]:
            s[i] = dices[i]
            for j in range(i-1, max(i-s[i]-1, 0), -1):
                if s[j] > 0:
                    s[j] -= 1
                else:
                    break
        else:
            s[i] = s[i-1] + 1

    return (n + 1) - s.count(0)
    
if __name__ == "__main__":
    
    t = int(input())
    for i in range(t):
        n = int(input())
        dices = [0] + list(map(int, input().split()))
        dices.sort()
        
        ans = solution()
        print(f"Case #{i + 1}:", ans)
