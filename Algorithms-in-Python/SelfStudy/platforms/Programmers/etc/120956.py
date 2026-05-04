def solution(babbling):
    answer = 0
    for word in babbling:
        p = 0
        length = len(word)
        while p < length:
            # print("word, p:", word, ",", p)
            left_word = len(word[p:])
            if left_word <= 1: break
            elif left_word == 2:
                if word[p:p+2] == "ye" or word[p:p+2] == "ma":
                    answer += 1
                break
            elif left_word == 3:
                if word[p:p+3] == "aya" or word[p:p+3] == "woo":
                    answer += 1
                    break
                else:
                    p += 1
            else:
                if word[p:p+3] == "aya" or word[p:p+3] == "woo":
                    p += 3
                elif word[p:p+2] == "ye" or word[p:p+2] == "ma":
                    p += 2
                else:
                    break
    return answer

import re

def solution_1(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt

def solution_2(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c

def solution_3(babbling):
    return len(list(filter(lambda x: x.replace("aya", "").replace("ye", "").replace("woo", "").replace("ma", "") == "" and "ayaaya" not in x and "yeye" not in x and "woowoo" not in x and "mama" not in x, babbling)))

if __name__ == "__main__":
    # babbling = ["aya", "yee", "u", "maa", "wyeoo"]
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    answer = solution(babbling)
    print(answer)