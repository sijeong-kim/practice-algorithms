def solution(n, lost, reserve):
    # 체격 순으로 매겨져 있어 
    # 앞번호, 뒷번호 학생에게만 체육복을 빌려줄 수 있음
    # 최대한 많은 학생이 체육수업을 들어야 함
    # 전체 학생 수 n
    # 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
    # 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
    # 체육수업을 들을 수 있는 학생의 최댓값을 return
    # 단, 여벌 체육복을 가져온 학생이 도난당한 경우 남은 체육복이 하나

    reserve = set(reserve)
    lost = set(lost)

    # 여벌을 가져온 학생은 자신의 체육복 사용
    both = reserve & lost
    lost -= both
    reserve -= both

    answer = n # 총 학생 수
    
    for l in lost:
        # 앞번호나 뒷번호 학생이 여벌을 가져왔는지 확인
        if l-1 in reserve: # 앞번호 먼저 확인
            reserve.discard(l-1)
        elif l+1 in reserve: # 뒷번호 확인
            reserve.discard(l+1)
        else: # 둘다 없다면
            answer -= 1
    
    return answer