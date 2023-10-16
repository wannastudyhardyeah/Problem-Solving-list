import re

def solution(new_id):
    pass

    size = len(new_id)

    # 1단계
    '''
    모든 대문자를 대응되는 소문자로 치환
    '''

    for i in range(size):
        temp_chr = ord(new_id[i])
        if (temp_chr >= 65 and temp_chr <= 90):
            new_id = new_id.replace(chr(temp_chr), chr(temp_chr + 32))
    print(new_id)


#    정규식 시도 흔적
    # p = re.compile(r"([A-Z])(.*)")

    # m = p.finditer(new_id)

    # sub_str = p.sub(, new_id)
    # print(sub_str)

    # for i in m:
    #     print(i.start())
    # print(m)

    # 2단계
    '''
    알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
    제외한 모든 문자 제거
    '''

    temp_id_str = new_id
    new_str = ""
    low_init = ord("a")
    low_fin = ord("z")

    num_init = ord("0")
    num_fin = ord("9")

    minus = ord("-")
    under_bar = ord("_")
    end_dot = ord(".")
    for i in range(size):
        temp_chr = ord(temp_id_str[i])
        if  ((temp_chr >= low_init and temp_chr <= low_fin)
            or
            (temp_chr >= num_init and temp_chr <= num_fin)
            or
            (temp_chr == minus)
            or
            temp_chr == under_bar
            or
            temp_chr == end_dot):
            new_str += chr(temp_chr)
        else:
            continue
    print("end:\n=>", new_str)
    new_id = new_str




    # 3단계
    '''
    마침표(.)가 2번 이상 연속된 부분을
    하나의 마침표(.)로 치환
    '''
    temp_id_str = new_id
    size = len(temp_id_str)
    pos = 0
    # 다음 문자가 '.'이면 1, 아니면 0
    is_next_dot = 0
    while(pos < size):
        # 이 조건은 '.'의 연속체 중에서
        #       첫 번째 만날 때만 분기하는 로직 돼야됨
        if (temp_id_str[pos] == '.'):
            # 첫번째 '.'의 위치
            init_pos = pos
            # 다음 문자도 '.'일 때만
            # 이걸 1씩 증가시킴
            fin_pos = pos
            is_next_dot = 1
            while(is_next_dot and fin_pos < size - 1):
                if (temp_id_str[fin_pos+1] == '.'):
                    fin_pos += 1
                else:
                    is_next_dot = 0
            # 차이가 날 때만 slice 후 '.' 하나 남김
            if (fin_pos - init_pos >= 1):
                front = temp_id_str[:(init_pos+1)]
                post = temp_id_str[(fin_pos+1):]
                temp_id_str = front + post
                # 사이즈 갱신
                size = len(temp_id_str)
                fin_pos = init_pos
        pos += 1
    print(temp_id_str)
    new_id = temp_id_str
    # 4단계
    '''
    마침표(.)가 처음이나 끝에 위치한다면
    제거
    '''
    size = len(new_id)
    if (size == 1):
        if (new_id == "."):
            new_id = ""
        else:
            pass
    else:
        if (new_id[0] == '.'):
            new_id = new_id[1:]
            size = len(new_id)
        if (new_id[size-1] == '.'):
            new_id = new_id[:(size-1)]
    print(new_id)

    # 5단계
    '''
    빈 문자열이라면
    new_id에 "a" 대입
    '''
    if (len(new_id) == 0):
        new_id = "a"

    # 6단계
    '''
    길이가 16자 이상이면
    new_id의 첫 15개 문자 제외한
    나머지 문자들 모두 제거
    
    만약 제거 후,
    마침표(.)가 new_id의 끝에 위치한다면
    끝에 위치한 마침표(.) 문자 제거
    '''
    print("6단계 시작")
    size = len(new_id)
    while (size >= 16):
        new_id = new_id[:15]
        size = len(new_id)
        if (new_id[size-1] == '.'):
            new_id = new_id[:(size-1)]
        size = len(new_id)
        print("now size:", size)
        print("now str:\n=>", new_id)
    print(new_id)

    # 7단계
    '''
    new_id의 길이가 2자 이하라면
    new_id의 길이가 3이 될 때까지
    new_id의 마지막 문자를
    반복해서 끝에 붙임
    '''
    size = len(new_id)
    while (len(new_id) <= 2):
        new_id = new_id + new_id[size - 1]
    print(new_id)
    answer = new_id
    return answer

if __name__ == "__main__":
    new_id = ["...!@BaT#*..y.abcdefghijklm",
              "........y..ABCd.",
              "a",
              "z-+.^.",
              "=.=",
              "123_.def",
              "abcdefghijklmn.p"]
    print(new_id)
    for i in new_id:
        solution(i)
