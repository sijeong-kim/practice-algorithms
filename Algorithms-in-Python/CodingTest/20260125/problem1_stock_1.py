
def solution(price):
    answer = [-1] * len(price)
    
    stack = []
    stack.append(0)    
    curr_index = 1
    
    while stack:
        
        if price[stack[-1]] < price[curr_index]:
            found_index = stack.pop()
            answer[found_index] = curr_index - found_index
        else:
            stack.append(curr_index)
            curr_index += 1
            
    return answer


price = [5, 3, 2, 3, 4, 7]

answer = solution(price)

print(answer)

price = [4, 1, 4, 7, 6]

answer = solution(price)

print(answer)

price = [13, 7, 3, 7, 5, 16, 12]

answer = solution(price)

print(answer)