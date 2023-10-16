import re


def search_option(origin_str):
    # '*'이나 '#'가 있으면 매칭시키기 위한 표현식
    for_option_match = re.compile('[*#]?')
    # 정규식으로 검사할 대상의 문자열
    str_for_reg = origin_str
        
    # iterable한 객체로 저장
    temp = for_option_match.finditer(str_for_reg)
    tuple_temp_for_return = {}
    cnt_for_tuple = 0
    for j in temp:
        # 튜플 형태로 받기
        span_temp = j.span()
        # 길이 구하기
        # (0이면 #이나 *가 없다는 뜻임)
        len_span = span_temp[1] - span_temp[0]
        # #이나 *가 있는 것만
        if (len_span == 1):
            # 시작, 끝 인덱스 출력
            print("start: ", j.start(), "end: ", j.end())
            # 해당 [#*] 출력
            print(j.group())
            # 리턴용 튜플에 저장하기
            tuple_temp_for_return[cnt_for_tuple] = (j.start(), j.group())
            cnt_for_tuple += 1
    print("----------------------") 
    return tuple_temp_for_return


""" 
3개로 나눠진 문자열 각각에 대해
리스트로 반환
e.g. - [1, 'S', '*']
"""
def check_parts(splits):
    # 스코어는 반드시 존재하므로
    # if문 필요없음
    for_score = re.compile('\d{1,2}')
    
    # 보너스도 반드시 존재
    for_bonus = re.compile('[SDT]')

    # 옵션은 존재할수도, 안 할수도
    for_option = re.compile('[*#]')
    # print("score: ", )
    # print("bonus: ", )
    # print("option: ", )
    
    option_val = for_option.search(splits)
    return_list = [for_score.search(splits).group(),
                   for_bonus.search(splits).group(),
                   (lambda option_val: option_val.group() if bool(option_val) is True else '')(option_val)]
    return return_list
    """ 
    - score
        same value

    - bonus
        S => power 1
        D => power 2
        T => power 3

    - option
        *(스타상) 
        => 첫 번째에 있으면
            첫 번째 점수에만 적용
           두 번째는
            첫 번째 있는 것과 중복적용 가능
            (*가 2개면 => 4배)
           세 번째는
            첫, 두 번째와 중복적용
            (*가 3개면 => 8배)
        
        #(아차상)
        => 아차상 나온 점수는 (-1) 곱함
     """

    return True

""" 
3개의 리스트가 담겨있는
1개의 리스트를 인자로 받음
그걸 각각 계산한 후
더하기

val_sharp_star_co
    : '*'와 '#'가 같이 있는지 
    체크 여부 받음
 """
def calcul_all(three_lists, val_sharp_star_co):

    # 합계를 위한 리스트
    for_sum = []
    idx = 0
    for i in three_lists:
        """
        현재 형태
        셋 다 str 타입임
        score는 숫자로 변환해야 편함 
        """
        score = int(i[0])
        bonus = i[1]
        option = i[2]

        
        # pow() 함수 인자 대응
        val_pow = [1, 2, 3]
        bonus_dict = {_:__ for _, __ in zip(['S', 'D', 'T'], [0, 1, 2])}
        
        for_sum.append(pow(score, val_pow[bonus_dict[bonus]]))

        if (option == '#'):
            for_sum[idx] = for_sum[idx] * (-1)
        elif (option == '*'):
            if (idx != 0):
                for_sum[idx - 1] = for_sum[idx - 1] * 2 
            # if (val_sharp_star_co is True):
            for_sum[idx] = for_sum[idx] * 2

        print(score, bonus, option)
        print(for_sum)
        if idx == 2:
            print(sum(for_sum))
        idx += 1

    result = sum(for_sum)
    return result

""" 
'*'과 '#'이 문자열에 같이 있으면
'#'(아차상)이 '*'보다 먼저 있어도
아차상 계산에도 2배를 곱해야 함
 => 동시에 존재하는지 파악해야됨
"""
def is_Sharp_and_Star_coexist(org_str):
    filter_for_coexist_sharp = re.compile('.*[#].*[*].*')
    filter_for_coexist_star = re.compile('.*[*].*[#].*')

    sharp_first = bool(filter_for_coexist_sharp.search(org_str))
    star_first = bool(filter_for_coexist_star.search(org_str))

    # 한쪽만 존재해도 
    # 둘 다 있는것이므로 OR 연산
    is_coexist = sharp_first | star_first
    # print("do sharp and star co-exist?\n=> ", )
    return is_coexist

if __name__ == "__main__":
    # p = re.compile('[1-10][SDT][*]?[#]?[1-10][SDT][*]?[#]?[1-10][SDT][*]?[#]?')
    p = re.compile('\d{1,2}[SDT][*#]?')
    str_for_re = "1D2S3T*"
    # '*'와 '#'이 같이 있는지 체크 먼저!
    val_sharp_star_co = is_Sharp_and_Star_coexist(str_for_re)
    # res = search_option(str_for_re)
    splits = p.finditer(str_for_re)

    all_lists = []
    for i in splits:
        temp = i.group()
        print("------------------\n", temp, "\n------------------\n")
        all_lists.append(check_parts(temp))

    calcul_all(all_lists, val_sharp_star_co)
    # is_Sharp_and_Star_coexist(str_for_re)

    # print(res)
    # for_num = re.compile('\d{1,2}')
    # for_score = re.compile('[SDT]')
    # for_option = re.compile('[*#]')
    # num = for_num.findall(str_for_re)
    # score = for_score.findall(str_for_re)
    # option = for_option.findall(str_for_re)


    # for_option_match = re.compile('[*#]?')
    # test_list = [
    #     '1S*10T#5*',
    #     '1S*10T#5',
    #     '1S*10T5',
    #     '1S10T#5*',
    #     '1S10T5*',
    #     '1S10T#5',
    #     '1S10T5'
    # ]
    # for i in test_list:
    #     # temp = for_option_match.findall(i)
    #     # print(for_option_match.finditer(i))
        
    #     # iterable한 객체로 저장
    #     temp = for_option_match.finditer(i)
    #     for j in temp:
    #         # 튜플 형태로 받기
    #         span_temp = j.span()
    #         # 길이 구하기
    #         # (0이면 #이나 *가 없다는 뜻임)
    #         len_span = span_temp[1] - span_temp[0]
    #         # #이나 *가 있는 것만
    #         if (len_span == 1):
    #             # 시작, 끝 인덱스 출력
    #             print("start: ", j.start(), "end: ", j.end())
    #             # 해당 [#*] 출력
    #             print(j.group())
    #     print("----------------------")
    # # print(for_option_match.findall(str_for_re))
    # # m = p.findall("1S2D*3T")
    # print(num)
    # print(score)
    # print(option)

    