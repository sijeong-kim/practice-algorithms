def solution(participant, completion):
    # 마라톤에 참여한 선수들의 이름이 담긴 배열 participant
    # 완주한 선수들의 이름이 담긴 배열 completion

    # 동명이인 있을 수 있음
    
    from collections import defaultdict
    
    hashmap = defaultdict(int)
    
    # 참가자 카운트
    for p in participant:
        hashmap[p] += 1
    
    # 완주자 차감
    for c in completion:
        hashmap[c] -= 1
    
    # 값이 1인 사람이 완주 못한 사람

    for name in hashmap:
        if hashmap[name] > 0:
            return name