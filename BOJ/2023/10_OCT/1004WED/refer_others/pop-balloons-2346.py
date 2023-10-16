# deque 사용 위해 collections 사용
from collections import deque

def solution(n, num_list):
    mapped_int_n_list = map(int, num_list)
    
    # enumerate로 하면
    # 인덱스(idx)랑 리스트 원소를
    # 같이 넘길 수 있음
    enum_of_int_n_list = enumerate(mapped_int_n_list)
    # rotate() 이용하기 위해 deque 사용
    queue = deque(enum_of_int_n_list)
    result = []

    while queue:
        #  enumerate로 묶은 리스트의
        # deque이므로 idx도 같이 받기
        #  그리고
        # a_popped로 하나 뽑아서 저장
        idx, a_popped = queue.popleft()
        # idx는 여기서
        # 각 풍선 번호 저장에 이용
        result.append(idx + 1)

        #  하나 뽑아 저장한 게
        # 양수라면
        if a_popped > 0:
            # 해당 양수만큼 오른쪽 이동
            # 이때, 전체 개수가 A개일 때
            # A개를 오른쪽으로 (n)만큼 이동은
            # (A-1)개를 왼쪽으로 (n-1)만큼 이동은
            # => 서로 동등
            queue.rotate(-(a_popped-1))
        # 음수라면
        elif a_popped < 0:
            # 해당 수만큼 왼쪽 이동
            queue.rotate(-a_popped)

    return result

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    solve = solution(n, num_list)
    print(*solve)