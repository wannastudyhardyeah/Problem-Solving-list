'''
프로그래머스
120866 - 안전지대
'''
'''
'''
def solution(board):
    divisr = len(board)
    all_idxs = len(board[0]) * divisr

    if (sum([board[i].count(1) for i in range(len(board))])
            == all_idxs):
        answer = 0
        return answer

    # 일단 모든 구역은 True로 설정
    # (위험구역일 시 => False)
    is_safe = [
        [True
         for j in range(len(board[0]))
         ]
        for i in range(len(board))]

    # 상하좌우, 모든 대각(상->상 / 시계) 좌표 계산
    # 0 1 2 3   4 5 6 7
    all_direcs = [[1, 0], [-1, 0], [0, -1], [0, 1],
                  [-1, 1], [1, 1], [1, -1], [-1, -1]]

    danger_cnt = 0

    for i in range(all_idxs):
        # 첫 번째 인덱스
        idx_1_dim = i // divisr
        # 두 번째 인덱스
        idx_2_dim = i % divisr

        temp_pick = board[idx_1_dim][idx_2_dim]

        if (temp_pick == 1):
            if is_safe[idx_1_dim][idx_2_dim] == True:
                is_safe[idx_1_dim][idx_2_dim] = False
                danger_cnt += 1
            for j in range(len(all_direcs)):
                r = all_direcs[j][0]
                c = all_direcs[j][1]
                try:
                    for_try = is_safe[idx_1_dim + r][idx_2_dim + c]
                except:
                    continue

                if c == 0:
                    # 상
                    if (idx_1_dim > 0
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1
                    # 하
                    if (idx_1_dim < divisr - 1
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1
                elif r == 0:
                    # 좌
                    if (idx_2_dim > 0
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1
                    # 우
                    if (idx_2_dim < divisr - 1
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1

                if r != 0 and c != 0:
                    # 상-우
                    if (idx_1_dim > 0
                            and idx_2_dim < divisr - 1
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1
                    # 하-우
                    if (idx_1_dim < divisr - 1
                            and idx_2_dim < divisr - 1
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1
                    # 하-좌
                    if (idx_1_dim < divisr - 1
                            and idx_2_dim > 0
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1
                    # 상-좌
                    if (idx_1_dim > 0
                            and idx_2_dim > 0
                            and is_safe[idx_1_dim + r][idx_2_dim + c] == True):
                        is_safe[idx_1_dim + r][idx_2_dim + c] = False
                        danger_cnt += 1

        # print(f"[{idx_1_dim}][{idx_2_dim}]")
    one_size = len(board)
    for i in range(one_size):
        for j in range(one_size):
            if is_safe[i][j] == True:
                print("1", end=' ')
            else:
                print("0", end=' ')
        print()

    safe_cnt = one_size * one_size - danger_cnt
    print(f"safe_cnt: {safe_cnt}")
    answer = safe_cnt
    return answer

if __name__ == '__main__':
    board = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
    solve = solution(board)
    print(solve)