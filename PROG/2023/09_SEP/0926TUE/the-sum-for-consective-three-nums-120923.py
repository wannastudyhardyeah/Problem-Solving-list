'''
프로그래머스
120923 - 연속된 수의 합
'''
'''

'''
from collections import deque

def solution(num, total):
    if (num == 1):
        answer = [total]
        return answer

    init_num = total // num + 1
    init_list = [init_num + i
                 for i in range(num)]

    # 내림차순으로 해서
    # 큰 수를 빼고
    # (최솟값 - 1)을 append
    queue = deque(sorted(init_list, reverse=True))

    sum_q = sum(queue)

    if (sum_q == total):
        answer = list(queue)
        return answer
    # 일단 아닌 상태로 시작
    # (종료 조건 비만족 위해서)
    while(sum_q != total):
        # 가장 큰 값 빼고
        queue.popleft()
        least = queue[-1]
        queue.append(least - 1)
        # 합을 갱신
        sum_q = sum(queue)
        # print(f"now queue: {queue} / sum: {sum_q}")

        if sum_q < total:
            break
    answer = sorted(list(queue))

    return answer

if __name__ == '__main__':
    num = 3
    total = 0
    solve = solution(num, total)
    # possible_list = []
    # for i in range(1, total//2 + 1):
    #     solve = solution(i, total)
    #     if (sum(solve) == total):
    #         possible_list.append(solve)
    #         print(f"\"{i}\"\n{solve}")
    print(solve)