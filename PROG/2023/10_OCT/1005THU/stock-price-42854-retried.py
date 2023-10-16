from collections import deque


# 다른 사람 풀이
'''
n: (prices의 길이) 일 때,
최악의 경우?
 => 각 가격이 완만하게 증가
            &
    가격 범위는 [1, 10000]일 때.
 => 최대 가격 범위의 차이 < 최대 길이 이므로
 => 최악 시간복잡도 O(n^2) 되게 하는 경우는 매우 적음(?)
    생각할 수 있는 최악: [1, 1, 1, 2, 2, 3, ..., 
                            9997, 9997, 9998, 9998, 9999, 10000]
for-i 에선 n
'''
def solution_other(prices):
        answer = []
        size_prices = len(prices)
        for i in range(size_prices - 1):
            total_time_cnt = 0
            for j in range(i, size_prices - 1):
                if(prices[i] <= prices[j]):
                    total_time_cnt += 1
                else:
                    break
            answer.append(total_time_cnt)
        answer.append(0)
        return answer


def solution(prices):
    '''
    [input]
    prices
        : 초 단위로 기록된 주식가격 담긴 배열
    ==
    [return]
    (list) : 각 가격마다
            그 가격 안 떨어진 시간 몇 초인지 기록
    '''
    '''
    '가격' 원소 하나만 넣지 말고
    => [가격, 입력 시각(초)의 리스트]

    Q. 각 원소들
     몇 초간 가격 유지됐는지는 어떻게 구하는가?
     => 최종 시간(초) 카운트 누적시간에서
        각 초를 빼는 식으로 구하기
    (이때 한 번 순회 필요함)

    그리고
    매번 append 할 때마다
    넣는 원소와, 스택의 (-1)번째 원소를
    서로 비교함
    넣는 원소가 작은 경우
    스택의 해당 (-1)번째 원소를 pop함.

    
    여기서 각 가격의 시간(초)
    ==> 가격 중복은 있어도 시간 중복은 없다
    '''
    size_of_prices = len(prices)

    # '스택'으로 시작하기


    # [해당 가격 개수, 입력된 시각(초)] 형식
    # ex) [가격, [1(초), 3(초), 4(초), ...] ] 이런 식으로
    prices_to_2dim = [[prices[_], (_+1)] for _ in range(size_of_prices)]
    # # reverse로 첫 번째 원소가 마지막 오도록 함
    # prices_to_2dim.reverse()
    print(prices_to_2dim)

    # 각 초마다 몇 초 유지됐는지
    # 기록하는 리스트
    # => 이게 return 될 예정
    result_calculated = [-1 for _ in range(size_of_prices)]
    # print(result_calculated)

    # 여기에 prices_to_2dim의 각 원소(2차원)를 넣음
    stack_that_prices_insrt = []
    
    # 누적 시간(초) 카운트
    total_time_cnt = 0
    # [[가격, 시각(초)], ...] 형식

    while(prices_to_2dim != []):
        # 시간 카운트는 먼저
        total_time_cnt += 1
        if (stack_that_prices_insrt == []):
            temp_price_pick = prices_to_2dim.pop()
            stack_that_prices_insrt.append(temp_price_pick)
            continue
        # 스택의 최상위 원소 참조
        stack_top = stack_that_prices_insrt[-1]
        # prices의 첫 번째 원소 참조
        temp_price_pick = prices_to_2dim[-1]
        # 새로 넣는 값이 스택 최상위 값보다 작을 때
        while(stack_top[0] > temp_price_pick[0]):
            # 해당 스택 최상위 값 꺼내고
            stack_that_prices_insrt.pop()
            # 그 최상위 값에 대한 시간(초) 기록
            result_calculated[stack_top[1]-1] = total_time_cnt - stack_top[1]
            # 스택 pop했으므로 range out 고려
            if (stack_that_prices_insrt != []):
                stack_top = stack_that_prices_insrt[-1]
                temp_price_pick = prices_to_2dim[-1]
        stack_that_prices_insrt.append(temp_price_pick)
        prices_to_2dim.pop()

        print(f'stack: {stack_that_prices_insrt}')
        print(f'prices: {prices_to_2dim}')

    for i in stack_that_prices_insrt:
        temp_stack_top = i[1]
        result_calculated[temp_stack_top-1] = total_time_cnt - temp_stack_top

    answer = result_calculated
    return answer



if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    solve = solution_other(prices)
    print(solve)

