import numpy as np
'''
같은 것 2개를 없앰

res_cnt: 누적된 값 그대로 받음
'''

def sames_pop(stack_list, res_cnt):
    size = len(stack_list)
    # # 뒤집어놓고 시작
    # stack_list.reverse()

    if (stack_list[size - 1] == stack_list[size - 2]):
        stack_list.pop()
        stack_list.pop()
        res_cnt += 2

    # # 1개면 비교 불가
    # # index 갱신 해야해서
    # # while { for{} } 구조로
    # while (size >= 2):
    #     is_not_same_things = 0
    #     # 마지막까지 가면 안됨
    #     for i in range(0, size - 1):
    #         size = len(stack_list)
    #         if (stack_list[i] == stack_list[i + 1]):
    #             pop_number = stack_list[i]
    #             # stack_list.reverse()
    #             stack_list.remove(pop_number)
    #             stack_list.remove(pop_number)
    #             res_cnt += 2
    #             # # size 갱신
    #             # stack_list.reverse()
    #             size = len(stack_list)
    #             print("POP!!!")
    #             # for문 나간 뒤
    #             # size가 2 이상이면
    #             # 다시 for문 진입
    #             break
    #         # 위 if문에 break 있어서
    #         # 여기까지 왔다는 건
    #         # 해당 i번째는 같은거 없다는 것
    #         if (i == size - 2):
    #             is_not_same_things = 1
    #         # else:
    #         #     if (size == 3 and i == 1):
    #         #         is_not_same_things = 1
    #         #         break
    #         #     elif (size == 2):
    #         #         is_not_same_things = 1
    #         #         break
    #     if (is_not_same_things == 1):
    #         break
    # stack_list.reverse()
    return res_cnt

def sames_pops(stack_list, res_cnt):

    size = len(stack_list)
    # 1개면 비교 불가
    # index 갱신 해야해서
    # while { for{} } 구조로
    while (size > 1):
        size = len(stack_list)
        # if (size == 2
        #     and
        #     stack_list[0] != stack_list[1]
        # ):
        #     break
        # else:
        # range out 고려
        is_not_same_things = 0
        for i in range(size - 1, 0, -1):
            size = len(stack_list)
            if (stack_list[i] == stack_list[i - 1]):
                pop_number = stack_list[i]
                stack_list.reverse()
                stack_list.remove(pop_number)
                stack_list.remove(pop_number)
                res_cnt += 2
                # # size 갱신
                stack_list.reverse()
                size = len(stack_list)
                print("POP!!!")
                # for문 나간 뒤
                # size가 2 이상이면
                # 다시 for문 진입
                break
            # 위 if문에 break 있어서
            # 여기까지 왔다는 건
            # 해당 i번째는 같은거 없다는 것
            if (i == 1):
                is_not_same_things = 1
            # else:
            #     if (size == 3 and i == 1):
            #         is_not_same_things = 1
            #         break
            #     elif (size == 2):
            #         is_not_same_things = 1
            #         break
        if (is_not_same_things == 1):
            break
'''
moves 그대로 받음
board 그대로 받음
stack_list 그대로 받음
    ㄴ 이건 처음엔 empty 상태
'''
def picking(moves, board, stack_list, first_nz_idxs):

    res_cnt = 0
    for idx_i, _ in enumerate(moves):
        # (one move의 값) - 1로 인덱스!!!
        pick_idx = _ - 1
        first_nz_pos = first_nz_idxs[pick_idx]
        # 아무것도 없는 column엔
        # 뽑을 것 없으므로
        if (first_nz_pos == len(board)):
            continue
        temp_pick = board[pick_idx][first_nz_pos]
        stack_list.append(temp_pick)
        print("picking number:", temp_pick)
        print("now stack:\n", stack_list)
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
            size = len(stack_list)
            if (stack_list[size - 1] == stack_list[size - 2]):
                stack_list.pop()
                stack_list.pop()
                res_cnt += 2
            # res_cnt = sames_pop(stack_list, res_cnt)
            print("now stack:\n(popped)\n", stack_list)
            print("now cnt:", res_cnt)
            # 같은 게 있으면
            # 바로 없애야 함
            # temp_cnt = sames_pop(stack_list, res_cnt)
            # res_cnt += temp_cnt
        print("-------------")
        print_now(board)
        print("-------------")
        # # 인덱스 업데이트
        # np.transpose 해서, 이건 필요없어짐
        # idx_board[pick_idx] = update_idxs(board, pick_idx)

        # for j in range(start_pos)
        # for idx, j in enumerate(board[pick_idx]):
        #     temp_pick = j
        #     if (temp_pick != 0):
        #         stack_list.append(temp_pick)
        #         print("picking number:", temp_pick)
        #         # 같은 게 있으면
        #         # 바로 없애야 함
        #         res_cnt = sames_pop(stack_list, res_cnt)
        #         # 인덱스 업데이트
        #         idx_board[pick_idx] = update_idxs(board, pick_idx)
        #         print("now stack_list\n:", stack_list)
        #         print("now cnt:", res_cnt)
        #         board[pick_idx][idx] = 0
        #         print_now(board)
        #         print("----------")
        #         # 첫 non-zero 찾으면 종료
        #         break
    return res_cnt


'''
처음으로 nonzero인 idx
(이걸 구해놔야
 리스트 참조 횟수 줄임)
'''
def first_nonzero_idxs(board):
    first_nz_idxs = [-1, -1, -1, -1, -1]
    for pos_i, i in enumerate(board):
        finded_first_nz = (0, -1) # (bool, <int>idx)
        for pos_j, j in enumerate(board[pos_i]):
            if (j != 0):
                finded_first_nz = (1, pos_j)
                break
        if finded_first_nz[0] == 1:
            first_nz_idxs[pos_i] = (finded_first_nz[1])
        else:
            first_nz_idxs[pos_i] = len(i)

    return first_nz_idxs

def first_nonzero_idx(board):
    first_nz_idxs = [-1, -1, -1, -1, -1]
    size = len(board)
    for i in range(size):
        for j in range(size):
            if (board[i][j] != 0):
                first_nz_idxs[i] = j
                break
    return first_nz_idxs

def print_now(board):
    for a in range(len(board)):
        for b in range(len(board[a])):
            print(board[a][b], end=' ')
        print('')

if __name__ == "__main__":
    main_func = [1, 2, 3, 4, 5, 6]
    a_func(main_func)
    print(main_func)