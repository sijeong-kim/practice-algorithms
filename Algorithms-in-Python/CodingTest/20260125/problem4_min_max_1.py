# def find_max_value(sample):

#     max_value = -1
#     characters = set(sample)
#     for char in characters:
#         max_value = max(sample.count(char), max_value)
        
#     return max_value


    
def solution(s, n):

    # n번 분할로 k 최대 중복 문자수 가능? (greedy, hashmap)
    def is_possible(k): # k
        
        splits = 0 # 자른 횟수
        
        counts = {}
                
        for char in s:
            
            if counts.get(char, 0) + 1 > k:
                splits += 1
                counts = {char: 1}
            
                if splits > n:
                    return False
            else:
                counts[char] = counts.get(char, 0) + 1
        
        return True

    # 최소 최대 매개변수 이진 탐색
    answer = len(s)
    
    # 답의 범위 설정
    start = 1
    end = len(s)
    
    while start <= end:
        mid = (start + end) // 2 # 최대 중복 문자수 k
        
        if is_possible(mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


s = "aabbbabba"
n = 2
answer = solution(s, n)
print(answer)

s = "xyyyyxxxxxx"
n = 2
answer = solution(s, n)
print(answer)

s = "abcd"
n = 1
answer = solution(s, n)
print(answer)
