def solution(arr):
    
    # 0~9 로 이루어져 있음
    # 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    # 제거 후 남은 숫자 반환할때 배열 arr의 원소들의 순서 유지
    
    # stack에 숫자 남기기 top 과 같으면 넣지 않기 stack을 리턴
    stack = []
    for a in arr:
        if stack and stack[-1] == a:
            continue
        stack.append(a)
        
    return stack