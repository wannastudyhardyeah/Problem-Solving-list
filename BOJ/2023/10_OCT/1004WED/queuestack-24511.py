from collections import deque

def solution(n, qu_or_st, dt_strctr,
             len_to_be_inserted, to_be_inserted):
    '''
    2차원 배열 생각해보기
    => 1차원 그대로 해도 되지 않을까?
        어차피 각 "자료구조"마다 보존되는건 원소 1개임
        2차원은 불필요하다고 생각됨

    (i) A = 0일 때
    기존의 수가 나가고,
    들어온 수가 보존된다
    (ii) A = 1일 때
    들어온 수가 나가고
    기존의 수가 보존된다.

====>  이건 결국 A=0인 경우에 대하여만
    찾는 문제임
    즉, A=0이 연속인 부분들은
    1칸씩만 rotate하고
    맨 왼쪽엔 그보다 1칸 왼쪽의 A=1인 부분이,
    맨 오른쪽은 맨 왼쪽에 있었던 수가 감
    
    A=1인 부분은 숫자도 신경 안써도 됨!
    '''
    # 수열 A(큐 or 스택 정보)
    A_qu_or_st = qu_or_st
    # 수열 B(자료구조 원소들)
    B_contents_nums = dt_strctr
    # 수열 C(삽입할 원소들)
    C_nums_to_be_input = to_be_inserted
    C_nums_size = len_to_be_inserted

    # - 길이 N으로 범위
    # - 수열 A로 인덱싱(idx로) 참조
    # - 수열 B로 값 참조해서 얻기
    # - 수열 C로 수열 B와 자료구조 실행.

    # 리턴값 하나씩 담을 리스트
    # deque로 만들기
    result = deque([])

    # for문 범위
    #   : "자료구조의 개수"만큼 반복
    for idx, a_B_ds_num_be_input in enumerate(B_contents_nums):
        # A의 idx번째(오직 queue 경우만 참조)
        if A_qu_or_st[idx] == 0:
            result.appendleft(a_B_ds_num_be_input)
        else:
            if (result is []):
                print(*C_nums_to_be_input)
                return;

    # for문 - 범위
    #   : "입력할 수열의 개수"만큼 반복
    for a_num_be_input in C_nums_to_be_input:
        result.append(a_num_be_input)
        result_popped_for_print = result.popleft()
        print(result_popped_for_print, end=' ')

    return;

import sys
import random as rd

# # 정규식을 위한 전처리
# str_A = ''.join([str(_) for _ in A_qu_or_st])
#
# # print('str:', str_A)
# # 정규식 써보기
# p = re.compile('[0]{2,}')
# m = p.finditer(str_A)
# for i in m:
#     tmp = i.span()
#     print(tmp[1] - tmp[0])

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    qu_or_st = list(map(int, sys.stdin.readline().split()))
    dt_strctr = list(map(int, sys.stdin.readline().split()))
    len_to_be_inserted = int(sys.stdin.readline())
    to_be_inserted = list(map(int, sys.stdin.readline().split()))

    # test_A_list = [rd.randint(0, 1) for _ in range(100000)]
    # qu_or_st = [0, 1, 1, 0]
    # print(f'{n}\n{qu_or_st}\n{dt_strctr}\n{len_to_be_inserted}\n{to_be_inserted}')
    solve = solution(n, qu_or_st, dt_strctr,
                     len_to_be_inserted, to_be_inserted)
