'''
프로그래머스
42626 - 더 맵게
'''
import heapq

'''
    scoville의 원소들을
    'K 미만'과 'K 이상'인 것으로 분리?
     => 이건 보류함 일단
'''
def solution(scoville, K):
    orgn_len = len(scoville)
    heapq.heapify(scoville)

    while(scoville[0] < K):
        len_scoville = len(scoville)
        # 길이가 1인 경우
        if len_scoville == 1:
            # 첫 번째에도 K 미만이 없다
            # => K 미만인 것이 하나도 없다
            if scoville[0] < K:
                return -1
            else:
                # 섞은 횟수
                # = (원래 원소개수) - (현재 원소개수)
                total_cnt_to_K = orgn_len - len(scoville)
                return total_cnt_to_K
        # 길이가 2 이상인 경우
        else:
            # 첫 번째, 두 번째 삭제, 저장
            # (즉, 1번째로/2번째로 작은 값)
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            # 문제에 제시된, 섞을 때의 식
            a_new_scov = first + second*2
            # 섞어서 새로 생성된 1개의 값을 넣음
            heapq.heappush(scoville, a_new_scov)
            print(f'a_new_scov: {a_new_scov}')

    # # less_vals = []  # K 미만
    # # eq_or_big_vals = [] # K 이상
    # # for _ in scoville:
    # #     if (_ < K):
    # #         less_vals.append(_)
    # #     else:
    # #         eq_or_big_vals.append(_)
    # # print(f'less_vals: {less_vals}\neq_or_big_vals: {eq_or_big_vals}')
    total_cnt_to_K = orgn_len - len(scoville)
    return total_cnt_to_K

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    solve = solution(scoville, K)
    print(solve)