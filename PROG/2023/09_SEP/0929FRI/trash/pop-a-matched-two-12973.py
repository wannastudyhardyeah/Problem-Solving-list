import re
from re import Match
from typing import Iterator

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
def solution(s):
    answer = -1
    string = s
    regexp = re.compile(r'(.)\1*')
    # matched_list = regexp.finditer(string)

    # 최초의 반복부분문자열 제외하곤 다 들어감
    str_list = []
    str_merged = ''
    been_came_to_end = 0
    matched_list = list(regexp.finditer(s))
    len_mached_list = len(matched_list)
    idx = 0
    # 여기에 최초 반복부분문자열 빼고
    # 다 plus하기
    now_str = ''
    while(been_came_to_end != 1):
        there_not_repeated = 1
        idx = 0
        while (idx != len_mached_list):
            temp_str_pick = matched_list[idx].group()
            # 반복부분문자열 찾으면
            if (len(temp_str_pick) >= 2):
                if (there_not_repeated == 0):
                    now_str += temp_str_pick
                    print(f"{idx}, {temp_str_pick}")
                else:
                    # 반복 존재 flag 변경
                    there_not_repeated = 0
                    idx += 1
                    continue
            else:
                if (idx + 1 == len_mached_list
                    and there_not_repeated == 1):
                    been_came_to_end = 1
                now_str += temp_str_pick
                print(f"{idx}, {temp_str_pick}")
            idx += 1
        print(f"now_str: {now_str}")
        # string에 대해 정규식 적용
        # (매 차례 갱신해야 함)
        if (now_str == ''):
            answer = 1
            break
        else:
            if (been_came_to_end == 1
                and there_not_repeated == 1):
                answer = 0
                print("final iteration: NOT REPEATE!!!")
        matched_list = list(regexp.finditer(now_str))
        len_mached_list = len(matched_list)
        now_str = ''


        # for idx, match in enumerate(matched_list):
        #     temp_str_pick = match.group()
        #     # str_list.append(temp_str_pick)
        #     # 같은 문자가 반복되는 게
        #     # 최초로 나오는 것만 선택!
        #     if (len(temp_str_pick) >= 2
        #             and been_came == 0):
        #         # str_list.pop(idx)
        #         # print(temp_str_pick)
        #         there_not_repeated = 1
        #         continue
        #     if there_not_repeated == 0:
        #         str_merged += temp_str_pick

    # # 반복부분문자열 있는지 체크
    # # (이걸로 while break 조건)
    # there_not_repeated = 0
    # while(there_not_repeated == 0):
    #     for idx, match in enumerate(matched_list):
    #         temp_str_pick = match.group()
    #         # str_list.append(temp_str_pick)
    #         # 같은 문자가 반복되는 게
    #         # 최초로 나오는 것만 선택!
    #         if (len(temp_str_pick) >= 2
    #                 and been_came == 0):
    #             # str_list.pop(idx)
    #             # print(temp_str_pick)
    #             there_not_repeated = 1
    #             continue
    #         if there_not_repeated == 0:
    #             str_merged += temp_str_pick
    # print(str_list)
    # print(f"merged: {str_merged}")


    # print(matched_list)
    return answer

if __name__ == '__main__':
    s = "baabaa"
    solve = solution(s)
    print(solve)