import sys
input = sys.stdin.readline

def solution(string):

    cnt = 0
    score = 0
    for i in range(len(string)):

        if string[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
        
    return score

string = input()
print(solution(string))