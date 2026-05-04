def solution1(participant, completion):
    participant.sort()
    completion.sort()
    n = len(participant)
    for i in range(n-1):
        if participant[i] == completion[i]:
            continue
        else:
            return participant[i]
    return participant[n-1]

# hashmap
def solution2(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 1. Hash : Participant의 dictionary 만들기
    # 2. Paticipant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다.
    return hashDict[sumHash]

import collections
def solution3(participant, completion):
    # 1. participant의 Counter를 구한다.
    # 2. completion의 Counter를 구한다.
    # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다.
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    # 4. counter의 key값을 반환한다.
    return list(answer.keys())[0]

print(solution3(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))