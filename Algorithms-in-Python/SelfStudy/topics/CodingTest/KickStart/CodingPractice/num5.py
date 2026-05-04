"""Starter Code for Milk Tea CC Problem"""

import itertools

# Complete the count_complaints function
def count_complaints(preferences, forbiddens):
    # TODO: Add logic to count the number of complaints
    
    results = list(itertools.product((['0', '1']), repeat=num_options))
    count = int(1e9)
    
    for result in results:
        result = ''.join(result)
        
        if result in forbiddens:
            continue
        
        # 최소 complaint 계산
        c = 0
        for preference in preferences:
            for i in range(num_options):
                if preference[i] != result[i]:
                    c += 1
        
        if c < count:
            count = c
                
    return count

if __name__ == '__main__':
    # Read number of test cases
    num_cases = int(input())

    for tc in range(1, num_cases + 1):
        # Read number of friends, number of forbidden teas, and number of options
        num_friends, num_forbidden, num_options = map(int, input().split())

        # Read the friends' preferences
        preferences = [input() for _ in range(num_friends)]

        # Read the forbidden teas
        forbiddens = [input() for _ in range(num_forbidden)]

        print("Case #%d: %d" % (tc, count_complaints(preferences, forbiddens)))
