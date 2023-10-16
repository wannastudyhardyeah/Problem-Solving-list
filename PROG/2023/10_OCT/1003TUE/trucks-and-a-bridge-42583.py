from collections import deque

def solution(bridge_length, weight, truck_weight):
    '''
    bridge_length [int]
        : 다리에 올라갈 수 있는 트럭 수
    weight  [int]
        : 다리가 견딜 수 있는 무게
    truck_weight [list]
        : 트럭별 무게
    '''
    '''
      여기서 트럭에 대한 고유id는 필요없음
    무게 중복되어도 상관없음
    단지 무게 하나에 트럭 하나를 
    맵핑해서 생각해도 됨
    
      단, 여기서 고려해야 할 점
    => (다리의 가능 무게) - (현재 건너는 트럭 무게 합)
    이 값이 대기 트럭의 0번째 트럭 무게보다 작을 때
    이 트럭은 또 대기를 해야 함
    이 경우는 특별하게 처리를 해야 할까, 괜찮을까?
    '''
    ############# 변수 준비 시작 #############
    # init상태의 트럭 총 개수
    num_of_trucks = len(truck_weight)
    # 경과 시간
    time_passed = 0
    ''' # 1. 대기 트럭 리스트
        # 2. 다리 건너는 트럭 리스트 
        # 3. 다리 지난 트럭 리스트'''
    waiting_truck_list = [] #1
    passing_truck_list = [] #2
    passed_truck_list = []  #3

    # 다리가 견딜 수 있는 무게.
    LIMIT_WEIGHT = weight
    # 다리에 올라갈 수 있는 트럭 수
    LIMIT_NUMS = bridge_length

    # init 대기 트럭은 곧 init무게 리스트
    waiting_truck_list = deque(truck_weight)
    passing_truck_list = deque([])
    # 트럭이 다리를 어디까지 건너갔는지 카운트
        # 각 값의 상한은 bridge_length까지임
    how_much_passed = deque([0 for _ in range(num_of_trucks)])
    ############# 변수 준비 끝 #############
    
    ### for test
    print ("{:<8} {:<18} {:<15} {:<8}".format('경과 시간',
                                              '다리 지난 트럭',
                                              '건너는 트럭',
                                              '대기 트럭'))
    print ("{:<12} {:<24} {:<19} {:<8}".format(time_passed,
                                               str(passed_truck_list),
                                               str(passing_truck_list),
                                               str(waiting_truck_list)))
     ###---------

    ############# 시뮬레이션 시작 #############
    # "종료조건"
    # 다리 지난 트럭 리스트의 길이가
    # 트럭 총 개수와 같아졌을 때 종료
    while(len(passed_truck_list) < num_of_trucks):
        # 1초 지남
        time_passed += 1

        # 건너는 트럭이 1개도 없으면 할 필요 X
        if (len(passing_truck_list)):
            temp_has_arrived = how_much_passed[0]
            # 시간 지난 트럭이 있다면
            if (temp_has_arrived >= bridge_length):
                # 패스 시키기
                temp_truck_ended = passing_truck_list.popleft()
                passed_truck_list.append(temp_truck_ended)
                # how_much_passed도 대응하여 popleft
                how_much_passed.popleft()

        # 현재 다리 위 트럭 수가
        # 가능 트럭 수와 같거나 크면 넘김
        if (LIMIT_NUMS <= len(passing_truck_list)):
            continue

        ################
        # 현재 가능한 무게 구하기
        # (견딜 수 있는 무게) - (건너는 트럭 총 무게)
        available_weight = LIMIT_WEIGHT - sum(passing_truck_list)
        if (len(waiting_truck_list) != 0):
            # 현재 대기트럭 큐의 첫 번째 트럭 선택
            # (건너기 불가능할 수도 있으므로 popleft는 나중에!)
            temp_truck_pick = waiting_truck_list[0]
            if (temp_truck_pick <= available_weight):
                # 트럭이 다리로 건너는 과정
                truck_progressed = waiting_truck_list.popleft()
                passing_truck_list.append(truck_progressed)

        # 현재 건너는 모든트럭의 시간 +1 하는 과정
        num_now_passing = len(passing_truck_list)
        for j in range(num_now_passing):
            if how_much_passed[j] < LIMIT_NUMS:
                how_much_passed[j] += 1

        ### for test-----
        print ("{:<12} {:<24} {:<19} {:<8}".format(time_passed,
                                                   str(passed_truck_list),
                                                   str(passing_truck_list),
                                                   str(waiting_truck_list)))
        ###---------

        ############# 시뮬레이션 끝 #############
    return time_passed

if __name__ == '__main__':

    bridge_length = 100
    weight = 100
    truck_weight = [10,10,10,10,10,10,10,10,10,10]

    test_cases = [[2, 10, [7,4,5,6]],
                  [100, 100, [10,10,10,10,10,10,10,10,10,10]],
                  [100, 100, [10]]]
    for _ in range(len(test_cases)):
        one_case = test_cases[_]
        solve = solution(one_case[0], one_case[1], one_case[2])
        print(solve)