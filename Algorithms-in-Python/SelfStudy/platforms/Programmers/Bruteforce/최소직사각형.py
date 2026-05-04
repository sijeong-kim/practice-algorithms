def solution(sizes):
    # sizes 모든 명함의 가로 길이 세로 길이 
    
    ans_w, ans_h = 0, 0
        
    for w, h in sizes:
        if w < h: w, h = h, w
        # w >= h 되도록
        
        if ans_w < w: ans_w = w
        if ans_h < h: ans_h = h
        
    # 모든 명함을 수납할 수 있는 가장 작은 지갑 사이즈
    return ans_w * ans_h