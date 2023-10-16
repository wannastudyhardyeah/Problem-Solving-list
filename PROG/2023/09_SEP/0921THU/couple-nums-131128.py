'''
프로그래머스
131128 - 숫자 짝꿍
'''
def solution(x, y):
    x_hash_cnt_list = [0 for _ in range(10)]
    y_hash_cnt_list = [0 for _ in range(10)]

    x_len = len(x)
    y_len = len(y)

    # x가 길이 작으면
    # x, y 서로 교환(편의상)
    if (x_len < y_len):
        temp = [x, x_len]
        x, x_len = y, y_len
        y, y_len = temp[0], temp[1]

    # 더 길이 긴 걸 범위로 삼기
    iter_range = x_len if x_len >= y_len else  y_len
    
    # 0부터 9까지만 할당!!
    for i in range(iter_range):
        x_temp = int(x[i])
        x_hash_cnt_list[x_temp] += 1
        if (i < y_len):
            y_temp = int(y[i])
            y_hash_cnt_list[y_temp] += 1

    print(f"x hash\n=> {x_hash_cnt_list}\n"
          f"y hash\n=> {y_hash_cnt_list}")

    # 개수가 0이 아닌 것만 찾기
    # 그리고 그중 idx 최댓값인 것
    not_zeros_x = [[i, [x_hash_cnt_list[i], y_hash_cnt_list[i]]]
                   if (x_hash_cnt_list[i] != 0
                       and y_hash_cnt_list[i] != 0)
                    else [i, -1]
                   for i in range(9, -1, -1)]
    str_merge = ""
    print(not_zeros_x)
    for i in range(10):
        # 개수가 적은 쪽 선택
        try:
            min_num = min(not_zeros_x[i][1])
        except:
            min_num = -1
        print(min_num, end=' ')
        if min_num == -1:
            continue
        add_val = not_zeros_x[i][0]
        for j in range(min_num):
            if (add_val == 0
                and str_merge == "0"):
                continue
            str_merge += str(add_val)
    print(f"\nthis str_merge:{str_merge}, len: {len(str_merge)}")
    print(not_zeros_x)


    if (str_merge == ""):
        answer = "-1"
    else:
        answer = str_merge


    return answer
'''
x, y 각각을 딱 O(n)으로 읽은 뒤에
그걸 리스트에 해시맵으로 하기
=> 각 숫자별로 개수 카운트하기
'''
import random as rd
import time as tm

if __name__ == '__main__':
    # str_x = [str(rd.randint(0, 9)) for _ in range(3000000)]
    # str_y = [str(rd.randint(0, 9)) for _ in range(2982121)]
    str_x = "100"
    str_y = "123450"
    start = tm.time()
    sovle = solution(str_x, str_y)
    end = tm.time()

    print(f"{end-start:.5f}")
