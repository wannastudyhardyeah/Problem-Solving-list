'''
프로그래머스
140108 - 문자열 나누기
'''
'''
문자열 s = "banana"
==> x = "b"
'''

def solution(s):
    input_str = s
    sum_cnt = 0
    first = input_str[0]
    seperated = input_str[1:]
    len_seperated = len(seperated)
    # 문자열 길이 = 1인 경우 종료
    # (종료 이후 sum_cnt + 1 해야함)
    while(len_seperated >= 1):
        # x인 거, 아닌 거 개수 세기
        x_part = 1
        not_x_part = 0

        for i in range(len_seperated):
            # 한 글자 읽기
            temp_pick_chr = seperated[i]
            if (temp_pick_chr == first):
                x_part += 1
            else:
                not_x_part += 1

            is_need_break = 1
            # x_part == not_x_part 체크
            # 여기서, 문자열 분리 해야함
            # ㄴ "i" 번째
            if (x_part == not_x_part):
                is_need_break = 0
                print(f"(pre) seperated: {seperated}")
                sum_cnt += 1
                '''
                b a n a n a
                0 1 2 3 4 5
                '''
                seperated = seperated[i+1:]
                first = seperated[0]
                len_seperated = len(seperated)
                print(f"(aft) seperated: {seperated}")
                break
            else:
                if (i + 1 == len_seperated):
                    is_need_break = 1

        sum_cnt += 1
        # is_need_break=1 하는 순간
        #  - 두 횟수가 다른 상태
        #           AND
        #  - 남은 부분이 없다면
        if (is_need_break == 1):
            break

    print(f"sum_cnt: {sum_cnt}")
    answer = []

    return answer

if __name__ == '__main__':
    s = "banana"
    solve = solution(s)
    print(solve)
