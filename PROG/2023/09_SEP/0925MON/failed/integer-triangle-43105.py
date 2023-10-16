'''
프로그래머스
43105 - 정수 삼각형
'''
'''
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

idx(출발->가능한 도착)
[0][0] -> [1][0], [1][1]

[1][0] -> [2][0], [2][1]
[1][1] -> [2][1], [2][2]

[2][0] -> [3][0], [3][1]

7 -> 4 : 73824
7 -> 5 : 73825, 73875, 73175, 78175
7 -> 2 : 73872, 73172, 73142, 78042
7 -> 6 : 73146, 78146, 78046, 78046
7 -> 5 : 78045

'''

'''
삼각형 리스트의 간선 리스트의 1차원 내부 구성은
[(맨 아래 길이) - 1 ]만큼이다.

원소 개수 구성은
2, 4, 6, 8, ..., N+2

'''
def make_edges_info(len_trngl):
    edges_list = [
                    [-1
                   for j in range((i+1)*2)
                   ]
                  for i in range(len_trngl-1)
                  ]
    return edges_list

def solution(triangle):
    # 삼각형 높이 = 배열 1차원의 길이
    len_trngl = len(triangle)
    
    # iterate 대상: 도착지 숫자
    # 리스트의 마지막 원소를 차례대로 조회
    len_targt = len(triangle[len_trngl-1])

    # 전역으로 초기화
    now_sum = -1 
    for i in range(len_targt):
        target = triangle[len_trngl-1][i]
        
        # 최초 시작 지점 설정
        now_node = triangle[0][0]
        now_pos = [0, 0]
        edges_info = make_edges_info(len_trngl)
        # 종료 조건
        # - target 찾았거나
        # - 현재 합보다 큰 기존 합 만났거나
        #  (즉, 새로 더하는 수 >= 현재까지 합)
        while(True):
            # 시작 노드의 값이
            # 곧 시작 합
            now_sum = now_node
            edges_info[0][0] = triangle[0][0] + triangle[1][0]
            edges_info[0][1] = triangle[0][0] + triangle[1][1]

            # 높이 기준으로 iterate
            for j in range(1, len(edges_info)):
                prev_sum = 0
                for k in range(len(edges_info[j])):
                    col_idx_1 = k - abs(j, k)
                    col_idx_2 = k - col_idx_1
                    edges_info[j][k] = (triangle[j][col_idx_1]
                                    + triangle[j+1][col_idx_2])

                    # next_node = triangle[j][k]
                    # refer_edge = edges_info[now_pos[0],
                    #                     now_pos[1] + k]
                    # if refer_edge != -1:
                    #     now_sum += refer_edge
                    # else:
                    #     now_sum += next_node
                    #     edges_info[now_pos[0],
                    #                 now_pos[1] + k] \
                    #         = now_sum
                    # # 다음 노드로 이동
                    # now_node = next_node
                    # now_pos = [j, k]



                break

    answer = []

    return answer

if __name__ == '__main__':

    triangle = [[7],
                [3, 8],
                [8, 1, 0],
                [2, 7, 4, 4],
                [4, 5, 2, 6, 5]]
    solve = solution(triangle)
    print(solve)