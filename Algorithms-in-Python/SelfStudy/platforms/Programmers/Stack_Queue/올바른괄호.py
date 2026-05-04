
def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else: # ')'
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    if not stack:            
        return True
    else:
        return False
    
    