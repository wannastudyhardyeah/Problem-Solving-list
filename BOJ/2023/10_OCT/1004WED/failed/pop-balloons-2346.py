from collections import deque

def solution(n, num_list):
    ''' 인덱스를 실제 리스트로 적용!!!
    (N-1)번 풍선의 오른쪽에 0번 풍선이 있다.
    0번 풍선의 왼쪽에 (N-1)번 풍선이 있다.
            N-2     N-3     N-4
        N-1                     ...
            0       1       2
    '''
    '''
    - 풍선 안의 숫자가
    (i) 양수 => 오른쪽
    (ii) 음수 => 왼쪽
    
    - 풍선 안의 [숫자]
    => [양수/음수에 대응 방향]으로 [숫자]만큼 이동
    '''
    '''
    순서에 주의하기!
    1. 풍선 참조
    2. 해당 풍선 제거
    3. x칸 만큼 이동한 칸의 풍선 참조
    --
    
    => 사용할 참조 및 메서드
     - 인덱스로 참조: [i]
     - 값으로 참조: index() 
     - 값 제거: remove()
      (값으로 제거하기 때문에 인덱스 변화 영향 X)
    '''
    # balloons = deque(num_list)
    # [풍선 값: 풍선번호]
    balloons_idx_dict = [[num_list[_], (_+1)] for _ in range(len(num_list))]
    balloons = deque(balloons_idx_dict)

    # 터뜨린 풍선 순서대로 '풍선번호' 기록
    popped_bllns = []

    #### 최초 행동 시작 => 0번 풍선 터뜨리기

    init_blln = balloons[0]
    size_of_all = len(num_list)
    # 풍선 값
    init_bln_val = init_blln[0] % size_of_all \
        if init_blln[0] >= 0 else -(abs(init_blln[0]) % size_of_all)
    # 풍선 번호
    init_num = balloons[0][1]
    popped_bllns.append(init_num)
    # 다음 풍선의 [풍선값, 번호] 리스트를 얻음
    next_blln = balloons[0+init_bln_val]
    balloons.remove(init_blln)
    ######## 최초 행동 끝


    while(balloons):
        if (len(balloons) <= 1):
            last_thing = balloons.pop()[1]
            popped_bllns.append(last_thing)
            break
        # 현재의 참조 풍선 인덱스
        # ([ , ] 꼴을 참조하기 위함)
        now_idx = balloons.index(next_blln)

        # 현재의 참조 풍선([ , ]꼴)
        now_blln = balloons[now_idx]
        # 현재의 풍선 번호
        now_num = now_blln[1]
        popped_bllns.append(now_num)
        # 현재 풍선의 총 개수
        now_size_blln = len(balloons) - 1
        # 현재풍선으로부터의 다음풍선 참조 idx 계산은
        # remove 하기 전에 해야함!!
        now_blln_idx = (now_blln[0]+now_idx) % now_size_blln \
            if (now_blln[0]+now_idx) >= 0 else -((abs(now_blln[0] + now_idx)) % now_size_blln)
        # 다음으로 참조할 풍선 값(x칸 이동 위해)
        # 이때 range out 오류 처리해야 함
        # (now_size_blln 이용)

        # now_real_idx = (abs(now_blln_idx) % now_size_blln) \
        #                 if now_blln_idx >= 0 else -(abs(now_blln_idx) % now_size_blln)
        next_blln = balloons[now_blln_idx]
        balloons.remove(now_blln)

    answer = popped_bllns
    return answer

import sys

if __name__ == '__main__':
    # # 풍선의 개수
    # n = 5
    # # 각 풍선 안의 종이(수 적혀있음)
    # num_list = [3, 2, 1, -3, -1]
    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    solve = solution(n, num_list)
    for idx, _ in enumerate(solve):
        if idx == len(solve) - 1:
            print(_)
        else:
            print(_, end=' ')