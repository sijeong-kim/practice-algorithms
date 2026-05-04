def solution(answers):
    # 1, 2, 3, 4, 5, ....
    # 2, 1, 2, 3, 2, 4, 2, 5, ...
    # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    
    sus = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    dividers = [len(su) for su in sus]
    
    cnts = [0] * 3
    
    for idx, ans in enumerate(answers):
        for j in range(3): # 어떤 수포자?
            if ans == sus[j][idx % dividers[j]]:
                cnts[j] += 1

    return [i+1 for i, cnt in enumerate(cnts) if cnts[i] == max(cnts)]
