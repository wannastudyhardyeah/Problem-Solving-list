def solution(priorities, location):
    '''
        - location에 대한 아이디어
        location의 값을 x라 할 때
        초기 priorities의 x번째 원소가
        몇 번째로 실행되는지를 return해야 함
        => priorities의 각 원소에 대한 idx 맵핑 필요

        그리고,
        "몇 번째로 실행되는지"를 위해서
        따로 변수를 둬서 count할 필요가 있음
    '''
    # 각 원소에 대해 idx 맵핑
    proc_queue = [[idx, _] for idx, _ in enumerate(priorities)]
    # 실행 카운트
    exec_cnt = 0
    
    while(proc_queue):
        # temp_pick = proc_queue.pop(0)
        # temp_pick_prior = temp_pick[1]
        # copy_queue = proc_queue.copy()
        temp_pick = proc_queue[0]
        temp_pick_prior = temp_pick[1]
        copy_queue = proc_queue.copy()

        print(f'==init==\nnow: [{proc_queue}]\ntemp_pick: {temp_pick}')
        '''
        1번 순회로 가장 큰 값을 찾은 이후에
        해당 값이 있는 위치까지만 pop 계속 하기
        (해당 값 앞에 있는 값들은 pop()-append() 반복 적용)
        '''
        for _iter in copy_queue:
            if (temp_pick_prior < _iter[1]):
                temp_pick = _iter
                temp_pick_prior = _iter[1]
        biggest_ele = temp_pick
        print(f'biggest: {biggest_ele}')
        print(f'now: {copy_queue}')

        for _iter in copy_queue:
    # pop() -> append() 반복 위한 코드
            temp_pop = proc_queue.pop(0)
            # 미리 찾아놓은 가장 큰 값까지 도달 시
            if (temp_pop == biggest_ele):
                # 해당 원소로 값을 업데이트함
                temp_pick = temp_pop
                print(f'-[iter: {temp_pop}]-\nnow: [{proc_queue}]\ntemp_pick: {temp_pop}')
                # 반복 종료로 현재 for문 탈출
                break
            else:
    # pop() -> append() 반복 위한 코드
                proc_queue.append(temp_pop)
                print(f'-NOT[iter: {temp_pop}]-\nnow: [{proc_queue}]\ntemp_pick: {temp_pop}')

        if (location == temp_pick[0]):
            print(f'got it\nthis is {exec_cnt+1}')
            return exec_cnt+1
        exec_cnt += 1

if __name__ == '__main__':
    # priorities = [1, 1, 9, 1, 1, 1]
    # location = 0
    priorities = [2, 1, 3, 2]
    location = 2
    solve = solution(priorities, location)
    print(solve)