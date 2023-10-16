import heapq as hq
from queue import PriorityQueue

'''
    이 문제의 관건
    1. '0'이 주어졌을 때는 가장 작은 값 출력
     => 이는 즉, 이 출력&제거 직전에는 heapify()가 되어있어야 함
        근데, 이 heapify는 입력이 0 아닐 때는 매번 할 필욘 없음
     => 그리고 출력&제거 직후엔 heapify()가 되어있어야 함.
        근데, 이게 꼭 직후일 필요는 없고, 마찬가지로
            입력이 0일 때의 직전에 수행하면 됨
    
    2. 절댓값으로 다뤄야 하기 때문에, 
        입력 시에는 ((abs_val), (origin_val)) 형식으로?
    
    3. 순서가 중요하다!
        => 우선순위 큐 사용
'''


def solution(input_list):
    '''
        입력: (절댓값, 원값) 형식으로 시작
    '''
    heap_list = PriorityQueue()
    for item in input_list:
        if (item[1] == 0):

            if heap_list.qsize() == 0:
                print(f'0')
                continue

            smallest_num = heap_list.get()
            # print(f'smallest_num: {smallest_num}')
            print(f'{smallest_num[1]}')
        else:
            heap_list.put(item)
        # print(f'============\ncurrent heap contents\n=> {heap_list}\n============')

    # print(f'heap_list: {heap_list}')
    return;


import sys

if __name__ == '__main__':

    _, *howmany = map(int, sys.stdin.buffer.read().split())
    # howmany = int(sys.stdin.readline().strip())
    list = []
    for i in howmany:
        input_for_heap = (abs(i), i)
        list.append(input_for_heap)
    # list = [(1, 1), (1, -1), (0, 0), (0, 0), (0, 0), (1, 1), (1, 1), (1, -1), (1, -1), (2, 2), (2, -2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    # print(list)
    solve = solution(list)