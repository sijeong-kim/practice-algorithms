import sys
input = sys.stdin.readline
                      
def solution():
    result = 0
    for order in orders:
        
        avail = 0
        avail_del = []
        for i in range(len(deliveries)):
            if deliveries[i][1] > order: continue
            if deliveries[i][0] <= order: continue
            avail += deliveries[i][2]
            avail_del.append(i)
        
        if avail >= u:
            need = u
            for i in avail_del:
                if deliveries[i][2] >= need:
                    deliveries[i][2] -= need
                    continue
                need -= deliveries[i][2]
                deliveries[i][2] = 0
            result += 1
        else:
            break
    return result

if __name__ == "__main__":
    t = int(input())
    cnt = 0
    while t > 0:
        t -= 1
        cnt += 1
        
        d, n, u = map(int, input().split())
        
        # delivery
        deliveries = []
        for _ in range(d):
            m, l, e = map(int, input().split())
            deliveries.append([m+e, m, l])
        deliveries.sort(key = lambda x : (x[0], x[1]))

        # order
        orders = list(map(int, input().split()))
        ans = solution()
            
        
        print(f"Case #{cnt}:", ans)


