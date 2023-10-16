'''
프로그래머스 - 이진 변환 반복하기
'''
import re

def solution(s):
    # 이진변환 횟수
    res_all_iters = 0
    # 제거된 모든 0 개수
    res_sum = 0

    str_temp = s[:]
    while (str_temp != "1"):
        p = re.compile("[0]")
        howmany_zero = p.finditer(str_temp)
        res_sum += sum(1 for _ in howmany_zero)

        p = re.compile("[1]")
        m = p.findall(str_temp)
        merge_n_to_str = str(''.join(m))
        size = len(merge_n_to_str)

        str_temp = bin(size).split("0b")[1]
        res_all_iters += 1

    answer = [res_all_iters, res_sum]
    return answer

if __name__ == '__main__':
    s = "110010101001"

    print(solution(s))