'''
프로그래머스
12951 - JadenCase 문자열 만들기
'''
'''
정규식 써보기
'''
import re
import collections

def solution(s):
    if (len(s) == 1):
        answer = s.upper()
        return answer
# 1단계: 공백에 대한 전처리
    p = re.compile("[^ ]+")
    space_reg = re.compile("[ ]+")
    # 공백으로 구분됨
    splited_by_space = p.findall(s)
    # 비-공백으로 구분됨
    splited_by_non_space = space_reg.findall(s)

# *** 만약 공백으로만 이뤄진 경우!!
#정규식에는 by_non_space에만 1개의 원소로 잡힘!!!
    if (len(splited_by_non_space) >= 1
        and len(splited_by_space) == 0):
        answer = splited_by_non_space[0]
        return answer
# -------------------------------
# 2단계: 첫 번째가 대문자인지?
    # (이건 iterate 함)

    if (len(splited_by_space) == 1):
        splited_by_space[0] = \
            (splited_by_space[0][0] + splited_by_space[0][1:].lower())

    else:
        for idx_1st, ele_1st in enumerate(splited_by_space):
            for idx_2nd, ele_2nd, in enumerate(ele_1st):
                #  숫자 판별은
                # 인덱스 0일 때만
                if idx_2nd == 0:
                    if ele_2nd.isnumeric() is True:
                        splited_by_space[idx_1st] = \
                            (ele_2nd + ele_1st[1:].lower())
                        break
                    else:
                        # 0번째가 숫자 아니면
                        # 바로 "대"+"소+"로 만들고 break
                        splited_by_space[idx_1st] = \
                            (ele_2nd.upper() + ele_1st[1:].lower())
                        break
                # 1번째부터는 숫자는 안 나옴!!!
                # 대/소문자만 나오는 것만 고려
                # 0번째가 숫자인 경우의 이후에만 여기로 옴
                else:
                    splited_by_space[idx_1st] = \
                        (ele_1st[0] + ele_2nd.upper()
                         + ele_1st[2:].lower())
                    break

    # print(splited_by_space)

# -------------------------------
    # 3단계: 공백 보존!!!!!!!!!!!!! 중요함!!

# -------------------------------
#     print(m)

    if len(splited_by_non_space) == len(splited_by_space):
        # 공백이 먼저 나올 때
        if (s[0].isalnum() is False):
            temp_concat = ''
            for number, ele_space in enumerate(splited_by_non_space):
                temp_concat = ele_space.join([f'{temp_concat}',
                                              f'{splited_by_space[number]}'])
        else:
            temp_concat = ''
            for number, ele_char in enumerate(splited_by_space):
                temp_concat = ele_char.join([f'{temp_concat}',
                                              f'{splited_by_non_space[number]}'])
    elif len(splited_by_non_space) > len(splited_by_space):
        temp_concat = splited_by_non_space[0]
        for number, ele_char in enumerate(splited_by_space):
            temp_concat = ele_char.join([f'{temp_concat}',
                                         f'{splited_by_non_space[number+1]}'])
    elif len(splited_by_non_space) < len(splited_by_space):
        temp_concat = splited_by_space[0]
        for number, ele_space in enumerate(splited_by_non_space):
            temp_concat = ele_space.join([f'{temp_concat}',
                                          f'{splited_by_space[number+1]}'])

    # if (space_reg.findall(s) == space_reg.findall(temp_concat)):
    #     print(f'OKAY')

    answer = temp_concat
    return answer

if __name__ == '__main__':
    s = "3people  unFollowed me"
    s_list = ["a",
              "                    ",
              "1                          a",
              " ",
              "3people  unFollowed me",
              "for the last week",
              "3peOple    UnFOLLoweD  1me",
              "3",
              "a b                                c  d e",
              "1a 2b 3c 4d 5e"]
    # solve = solution(s)
    for s_ele in s_list:
        solve = solution(s_ele)
        print(f's: "{s_ele}"\nsolve: "{solve}"')