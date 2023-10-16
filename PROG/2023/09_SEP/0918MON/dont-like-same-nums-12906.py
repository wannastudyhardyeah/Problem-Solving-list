def solution(arr):
    '''
    Stack
      - pop()
      - append()
      - top => -1
    '''
    stack = []
    # 스택의 가장 최근 입력 idx
    pointer = -1

    # 매개변수 arr의 크기
    arr_size = len(arr)

    for i in range(arr_size):
        temp = arr[i]
        if (pointer >= 0):
            if (stack[pointer] == temp):
                continue
        stack.append(arr[i])
        pointer += 1
    print(len(stack), pointer)

    answer = stack

    return answer

import random as ran

if __name__ == '__main__':

    arr = [ran.randint(1, 100) for _ in range(1000000)]
    # arr = [1, 1, 3, 3, 0, 1, 1]
    print(len(arr))
    solution(arr)