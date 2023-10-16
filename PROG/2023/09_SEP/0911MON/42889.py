""" 
index = 각 스테이지
( n번째 스테이지 => (n-1)번 )

=> 
    1. 각 스테이지별로 해당 스테이지 도달한 수
    2. 각 스테이지별로 해당 스테이지 도달 but 클리어 X
 """

def solution(N, stages):
    
    result = counting_stages(N, stages)
    answer = [result[i][0] for i in range(N)]
    # print(answer)

    return answer


def counting_stages(N, stages):

    # 유저의 수
    users_num = len(stages)
    """
      스테이지에 도달한 수를
    각 스테이지별 카운트하기 위해
    N개의 배열 생성

      즉, stages 배열의 각 원소마다
    해당 원소의 값만큼 loop 필요
    """
    reach_stages = [0 for _ in range(N + 1)]

    # 스테이지 도달 but NO 클리어 수
    no_clear_stages = [0 for _ in range(N + 1)]

    for i in stages:
        recent_reach = i
        if recent_reach == 1:
            reach_stages[0] += 1
            no_clear_stages[0] += 1
        elif recent_reach == 2:
            reach_stages[0] += 1
            reach_stages[1] += 1

            no_clear_stages[1] += 1
        else:
            # (해당 값 - 1)만큼 loop
            for j in range(recent_reach):
                reach_stages[j] += 1

            # 도달 but NO 클리어는 하나만!
            no_clear_stages[recent_reach - 1] += 1
    # print("reached stages\n==>", reach_stages)
    # print("reach but NO clear stages\n==>", no_clear_stages)

    fail_ratio = calcul_ratio(N, reach_stages, no_clear_stages)
    return fail_ratio

# 실패율 계산
def calcul_ratio(N, reach, no_clear):
    fail_ratio_list = [0 for _ in range(N)]

    for i in range(N):
        reach_val = reach[i]
        # div by zero 처리
        if reach_val == 0:
            fail_ratio_list[i]
        else:
            fail_ratio_list[i] = no_clear[i] / reach_val
    
    # 각 실패율과 인덱스 대응 필요!
    # for i in range(N):
    fail_ratio_dict = {
        (i+1) : fail_ratio_list[i] for i in range(N)
    }
    
    # print(fail_ratio_list)
    sorted_fail_ratio = sorted(fail_ratio_dict.items(), key=lambda x:x[1], reverse=True)
    # print(sorted_fail_ratio)
    # fail_ratio_list.sort(reverse=True)
    return sorted_fail_ratio

if __name__ == "__main__":
    N = 4
    stages = [4,4,4,4,4]
    solution(N, stages)