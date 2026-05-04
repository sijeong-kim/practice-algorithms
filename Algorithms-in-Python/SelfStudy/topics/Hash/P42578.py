def solution(clothes):
    hashmap = {}
    
    for cloth in clothes:
        if cloth[1] in hashmap:
            hashmap[cloth[1]] += 1
        else:
            hashmap[cloth[1]] = 1
        
    print(hashmap)
    ans = 1
    for val in hashmap.values():
        ans *= (val+1)
    
    return ans-1
        
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))