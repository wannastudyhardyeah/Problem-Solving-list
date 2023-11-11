def solution(progresses, speeds):
    '''
    조건
        1. 뒤에 있는 기능이 개발 완료되어도
            그 앞 기능이 개발 완료되어야 배포 가능
        2. 배포는 하루에 1번만 가능
        3. 배포는 하루의 끝에 이뤄짐
        e.g. 진도율 95%인 작업의 speed가 4%/d라면
            => 배포는 2일 뒤 이뤄짐

    아이디어
        - 스택의 최상위 부분
        : 맨 앞에 있는 기능
        - 작업의 진도율 계산
        : [(100% - (현 진도율)) / (해당 작업 speed)]
            + [1 if mod not zero, else 0]
    '''
    progresses = [[idx, _] for idx, _ in enumerate(progresses)]
    release_list = []
    print(progresses)

    coppied_progresses_for_iter = progresses.copy()
    # for idx, prog in coppied_progresses_for_iter:
    while(coppied_progresses_for_iter):
        print(progresses)
    #   배포한 개수 체크 변수
        release_cnt = 0

        temp_pick = coppied_progresses_for_iter[0]
        idx = temp_pick[0]
        prog = temp_pick[1]
        #  - 최상위 원소의 진도율 계산한 뒤
        # 해당 진도율에 따른 날짜만큼을
        # 그 이후 원소들에 진도율 적용시키기
        #  - idx로 해당 인덱스 대응하기
        
        # 이미 개발 완료되었으나(100 이상)
        # 앞에 있는 기능이 완료 안돼서 배포 안된 경우
        if (prog >= 100):
            # 이 경우엔 days를 1로 설정해야 맞음
            days = 1
        else:
            # 나눠지는 수 (남은 진도율)
            dividee = 100 - prog
            # 나누는 수 (각 기능의 개발 속도)
            divider = speeds[idx]
            # 진도율 계산
            days = (dividee) // divider + bool(dividee % divider)
        print(f'days: {days}')
    #   배포한 개수 체크 +1
        release_cnt += 1
        print(coppied_progresses_for_iter[0])
        coppied_progresses_for_iter.pop(0)

        # 리스트 한 개로 할 시엔
        # pop() 이뤄진 이후의 iter가 달라짐
        copy_progresses = coppied_progresses_for_iter.copy()
# ---------------------
#       나머지 기능들에 대한 진도율을 적용하는 파트
        for ele_pos, ele in enumerate(copy_progresses):
            temp_ele_idx = ele[0]
            temp_ele_prog = ele[1]
            # 진도율 구하기
            temp_result = temp_ele_prog + days * speeds[temp_ele_idx]
            if (temp_result >= 100
                    and coppied_progresses_for_iter[0] == ele):
                release_cnt += 1
                print(f'{ele, ele_pos}')
                coppied_progresses_for_iter.pop(0)
            # 진도율 100 이상 아니거나
            # 각 큐 반복마다 맨 앞 원소가 아닌 경우
            else:
                # 그땐 반드시 진도율 계산된 값 업뎃 필요
                copy_progresses[ele_pos][1] = temp_result
        print(f'release_cnt: {release_cnt}')
        release_list.append(release_cnt)

    answer = release_list
    return answer

if __name__ == '__main__':
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    solve = solution(progresses, speeds)
    print(solve)