import heapq
from collections import defaultdict


def solution(operations):
    min_heap = []
    max_heap = []
    count_number = defaultdict(int)  # 개수 세는 딕셔너리
    size = 0

    for operation in operations:
        op, number = operation.split()
        number = int(number)

        if op == 'D':

            if number == 1:  # 최대값 삭제
                while max_heap and count_number[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    count_number[max_val] -= 1
                    size -= 1

            else:  # 최소값 삭제
                while min_heap and count_number[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    count_number[min_val] -= 1
                    size -= 1

        else:  # I: 삽입
            size += 1
            heapq.heappush(max_heap, -number)
            heapq.heappush(min_heap, number)
            count_number[number] += 1  # 개수 추가

    if size == 0:
        return [0, 0]

    while max_heap and count_number[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    while min_heap and count_number[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    return [-max_heap[0], min_heap[0]]

if __name__ == "__main__":
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    # operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    print(solution(operations))