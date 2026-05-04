def solution(n, plans, clients): # 부가서비스 수, 요금제 정보, 고객 이용 서비스
    data = []
    service_to_id = {}
    for i, plan in enumerate(plans):
        p = list(map(int, plan.split()))
        d, ss = p[0], p[1:]
        data.append(d)
        for s in ss: service_to_id[s] = i
    
    answer = []

    for client in clients:
        c = list(map(int, client.split()))
        need_data, need_service = c[0], c[1:]
        
        flag = True
        tmp = []
        for s in need_service:
            if s not in service_to_id:
                flag = False
                break
            tmp.append(service_to_id[s])
        th = max(tmp)

        ans = -1

        # th = max([service_to_id[s] for s in need_service if s in service_to_id])
        # th + 1 이상 번호의 요금제만 가능
        if flag:
            for i in range(th, len(data)):
                if data[i] >= need_data:
                    ans = i
                    break

        answer.append(ans+1)

    return answer