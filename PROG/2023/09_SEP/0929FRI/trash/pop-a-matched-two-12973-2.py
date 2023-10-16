'''
최초의 반복부분문자열 체크
이 문자열 제거

    일단 while로 반복을 해서
  최초 반복부분문자열이 나올 때까지 반복!
  -> 하나도 없으면 끝까지 순회하고
    바로 종료한 뒤 "0" 출력하기

    해당 부분문자열의 앞뒤 부분문자열만 체크!
  (다 순회해서 다시 붙이고 하기엔
  문자열이 너무 긴 경우는 
  다 순회하기에는 안 될 것 같음)

  이때, 앞뒤 부분문자열을 붙였을 때
  반복되는 게 없을 시에만
  그 다음 부분을 체크!

'''
import re
def solution(s):
    answer = -1
    if len(s) == 1:
        answer = 0
        return answer
    # regexp = re.compile(r'(.)\1*')
    regexp = re.compile(r'(\w)\1')

    income_list_str = ''
    income_list_str += s[:2]
    s_idx = 2
    len_org_s = len(s)
    #  종료조건
    # : sub 적용 이전 문자열과
    # 이후의 문자열이 서로 같을 때임
    # (sub 적용 시 sub할 거 없으면 그대로 나옴)
    while(True):
        if (s_idx == 2):
            income_list_str = regexp.sub('',
                                         income_list_str,
                                         count=2)
        else:
            income_list_str = regexp.sub('',
                                     income_list_str,
                                     count=1)
        if s_idx == len_org_s:
            break
        check_others = regexp.sub('',
                                income_list_str[:-1] + s[:1],
                                count=1)
        print(check_others)
        if check_others != '':
            answer = 0
            return answer
        income_list_str += s[s_idx]
        s_idx += 1

    if income_list_str == '':
        answer = 1
    else:
        answer = 0

    return answer
# import random as rd
# import time as tm
if __name__ == '__main__':
    # list_abcd = ['a', 'b', 'c', 'd']
    # strs = ''
    # for _ in range(30000):
    #     randnum = rd.randint(1, 4)
    #     strs += list_abcd[randnum-1]
    # # print(strs)
    # start = tm.time()
    # print(solution(strs))
    # end = tm.time()
    # print(f"time: {end - start}")
    s_list = ["bbbb",
              "cdcd", "baabaa",
              "abbccdeef"]
    for s in s_list:
        solve = solution(s)
        print(solve)