def h_index(n, citations):
    ans = []
    # TODO: Complete the function to get the H-Index scores after each paper
    
    h = 0
    citations = list(citations)
    for i, c in enumerate(citations):
        if h <= c:
            cnt = 0
            for j in range(i+1):
                if citations[j] >= h+1:
                    cnt += 1
            if h+1 <= cnt:
                h += 1
        ans.append(h)

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        citations = map(int, input().split()) # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
