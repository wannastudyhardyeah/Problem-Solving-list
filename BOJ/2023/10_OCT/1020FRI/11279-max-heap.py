'''
    백준
    11279 - 최대 힙
'''
from queue import PriorityQueue

def solution(howmany_opers, int_arr_val_for_each_oper):
    ''' x가
          - 자연수 => 배열에 x 값 넣음
          - 0이면 => 가장 큰 값 출력하고 pop '''
    pri_queue = PriorityQueue()

    for idx, i in enumerate(int_arr_val_for_each_oper, start=1):
        # print(f'========\nPQ: {pri_queue}\n========')
        # i(x)가 자연수인 경우
        if (i > 0):
            # 해당 값 i를 큐에 넣음
            # minus를 붙여야 내림차순이 됨
            pri_queue.put(-i)
        # i가 0인 경우
        else:
            size_pq = pri_queue.qsize()
            # 아무 원소도 없는 경우
            if size_pq == 0:
                # 0 출력
                print(0)
            # 원소가 존재한다면
            else:
                # 가장 큰 원소를 꺼내서 출력
                # (이때, 우선순위 큐이므로 자동으로 최대 힙)
                temp_get_val = pri_queue.get()
                # 내림차순을 위해 minus 붙였기 때문.
                # print(f'big: {abs(temp_get_val)}')
                print(f'{abs(temp_get_val)}')

    return;

import sys

if __name__ == '__main__':
    # 연산의 개수
    howmany_opers = int(sys.stdin.readline().strip())

    int_arr_val_for_each_oper = []
    for i in range(howmany_opers):
        temp_input = int(sys.stdin.readline().strip())
        int_arr_val_for_each_oper.append(temp_input)

    solve = solution(howmany_opers, int_arr_val_for_each_oper)