'''
[프로그래머스]
12909 올바른 괄호

'''
def solution(s):
    '''
    - 맨 처음이 ')'이면 바로 False
    - 왼쪽cnt보다 오른쪽 cnt가 커지면
        False
    '''
    # 스택
    # stack = []
    # 스택의 포인터
    pointer_stack = 0
    # 왼쪽 괄호
    left_cnt = 0
    # 오른쪽 괄호
    right_cnt = 0

    size_s = len(s)
    is_right = True
    for i in range(size_s):
        temp = s[i]
        if (pointer_stack == 0 and temp == ")"):
            is_right = False
            break
        else:
            # stack.append(temp)
            pointer_stack += 1
            if (temp == "("):
                left_cnt += 1
            elif (temp == ")"):
                right_cnt += 1
            if (right_cnt > left_cnt):
                is_right = False
                break
    if (left_cnt != right_cnt):
        is_right = False

    answer = is_right

    return answer

if __name__ == '__main__':
    s = "(()("
    solution(s)