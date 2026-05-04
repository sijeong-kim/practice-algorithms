def solution(participant, completion):
    # 마라톤에 참여한 선수들의 이름이 담긴 배열 participant
    # 완주한 선수들의 이름이 담긴 배열 completion

    # 동명이인 있을 수 있음
    
    from collections import Counter
    
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
