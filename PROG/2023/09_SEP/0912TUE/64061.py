import numpy as np

'''
처음으로 nonzero인 idx
(이걸 구해놔야
 리스트 참조 횟수 줄임)
'''


def first_nonzero_idx(board):
    size = len(board)
    first_nz_idxs = \
        [next((i for i, x in enumerate(board[j]) if x), None) for j in range(size)]
    return first_nz_idxs


def solution(board, moves):
    board = np.transpose(board).tolist()
    # 쌓기 위한 리스트
    stack_list = []
    first_nz_idxs = first_nonzero_idx(board)

    res_cnt = 0
    for _ in moves:
        # (one move의 값) - 1로 인덱스!!!
        pick_idx = _ - 1
        first_nz_pos = first_nz_idxs[pick_idx]
        # 아무것도 없는 column엔
        # 뽑을 것 없으므로
        if (first_nz_pos == len(board)):
            continue
        temp_pick = board[pick_idx][first_nz_pos]
        stack_list.append(temp_pick)

        # pop을 했으므로 0으로 설정
        board[pick_idx][first_nz_pos] = 0
        # 빠지게 되면
        # 0이 늘어나므로 인덱스도 1 추가
        first_nz_idxs[pick_idx] += 1

        stack_size = len(stack_list)
        if (stack_size == 1 or stack_size == 0):
            continue
        elif (stack_size == 2 and (stack_list[0] != stack_list[1])):
            continue
        else:
            if (stack_list[stack_size - 1] == stack_list[stack_size - 2]):
                stack_list.pop()
                stack_list.pop()
                res_cnt += 2
    answer = res_cnt
    return answer

if __name__ == "__main__":
    solution()

    # board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    # board = np.transpose(board).tolist()
    # print(board)
    # moves = [1,5,3,5,1,2,1,4]
    # '''
    #     0 -> 4 -> 2 -> 4 -> 0 -> 1 -> 0 -> 3
    # '''
    # stack_list = []
    # first_nz_idxs = first_nonzero_idx(board)
    #
    # # print('\t', chr(32), end='')
    # # for j in range(len(board)):
    # #     print(j, end=' ')
    # # print('')
    # # for i in range(len(board)):
    # #     print(str(i) + "번", end=' : ')
    # #     for j in range(len(board[i])):
    # #         print(board[i][j], end=' ')
    # #     print('')
    #
    # print(picking(moves, board, stack_list, first_nz_idxs))




