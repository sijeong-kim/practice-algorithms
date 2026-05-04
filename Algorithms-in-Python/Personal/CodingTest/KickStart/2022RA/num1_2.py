# TIME LIMIT EXCEEDED
import sys
input = sys.stdin.readline

def solution(input_string, typing):


    if len(input_string) > len(typing):
        return "IMPOSSIBLE"
    
    x = 0
    for i in range(len(input_string)):
               
        if input_string[i] != typing[x]:
            while(input_string[i] != typing[x]):
                x += 1
                if x == len(typing):
                    return "IMPOSSIBLE"
        x += 1    
    
    return len(typing) - len(input_string)
            

if __name__ == "__main__":
    t = int(input())
    for idx in range(1, t+1):
        i = input().strip()
        p = input().strip()
        ans = solution(i, p)
        print(f"Case #{idx}: {ans}")