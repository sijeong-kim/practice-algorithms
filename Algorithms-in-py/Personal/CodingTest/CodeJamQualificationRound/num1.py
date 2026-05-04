
import sys
input = sys.stdin.readline
                      
def solution(r, c):
    for i in range(2 * r + 1):
        for j in range(2 * c + 1):
            row_r = i % 2
            row_c = j % 2
                
            if (i // 2 == 0 and j // 2 == 0) or (row_r == 1 and row_c == 1):
                print(".", end = '')
            elif row_r == 0 and row_c == 0:
                print("+", end = '')
            elif row_r == 1 and row_c == 0:
                print("|", end = '')
            else:
                print("-", end = '')
        print()

if __name__ == "__main__":
    t = int(input())
    cnt = 0
    while t > 0:
        t -= 1
        cnt += 1
        
        r, c = map(int, input().split())
        
        print(f"Case #{cnt}:")
        solution(r, c)
        
