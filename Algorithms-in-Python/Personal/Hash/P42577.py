# Sort/Loop을 사용
def solution1(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
        # if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True

# Hash를 사용
def solution2(phone_book):
    # 1. Hash map을 만든다.
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    # 2. 접두어가 Hash map에 존재하는지 찾는다.
    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if prefix in hash_map and prefix != phone_number:
                return False
    return True

# zip, startwith 사용
def solution3(phone_book):
    phone_book.sort()
    
    # https://www.daleseo.com/python-zip/
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startwith(p1):
            return False
    return True
    
    
print(solution2(["12","123","1235","567","88"]))