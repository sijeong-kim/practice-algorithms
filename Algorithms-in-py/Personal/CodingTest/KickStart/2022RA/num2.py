import sys
input = sys.stdin.readline

def solution(number):
    
    r = sum(map(int, number)) % 9
    if r != 0:
        r = 9 - r
    
    insert_digit = str(r)
    
    if insert_digit == "0":
        return number[0] + "0" + number[1:]
    
    for i in range(len(number)):
        if number[i] > insert_digit:
            return number[:i] + insert_digit + number[i:]
    
    return number + insert_digit
        

if __name__ == "__main__":
    t = int(input())
    for case in range(1, t+1):
        n = input().strip()
        ans = solution(n)
        print(f"Case #{case}: {ans}")
        
    