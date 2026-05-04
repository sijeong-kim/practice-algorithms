import sys
input = sys.stdin.readline
                      
def solution():
    total = M
    result = []
    for ink in inks:
        if total >= ink:
            result.append(ink)
            total -= ink
        else:
            result.append(total)
            total = 0
            
    return " ".join(map(str, result))

if __name__ == "__main__":
    M = int(1e6)
    IMP = "IMPOSSIBLE"
    
    t = int(input())
    for i in range(t):
        inks = [M] * 4
        
        for _ in range(3):
            c, m, y, k = map(int, input().split())
            inks[0] = min(inks[0], c)
            inks[1] = min(inks[1], m)
            inks[2] = min(inks[2], y)
            inks[3] = min(inks[3], k)
        
        if sum(inks) < M:
            ans = IMP
        else:
            ans = solution()
        print(f"Case #{i + 1}:", ans)

# 3
# 300000 200000 300000 500000
# 300000 200000 500000 300000
# 300000 500000 300000 200000
# 1000000 1000000 0 0
# 0 1000000 1000000 1000000
# 999999 999999 999999 999999
# 768763 148041 178147 984173
# 699508 515362 534729 714381
# 949704 625054 946212 951187
