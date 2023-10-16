from typing import List


'''
    "원 안에 점이 있다"의 정의는 어떻게 할 수 있을까?
     => 특정 점 P에 대하여
     (P의 x좌표, y좌표 및 원의 중심 사이의 거리)가
     원의 반지름보다 작거나 같은가? 를 따지기
'''

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 여러 개의 원들을 하나씩 반복

        # 쿼리 각각에 대한 내부 점 개수
        cnt_for_each_queries = []
        
        for one_query_crcl in queries:
            center_x = one_query_crcl[0]
            center_y = one_query_crcl[1]
            center_rad = one_query_crcl[2]

            # 내부 점의 개수 카운트
            num_of_inner_points = 0

            # 여러 개의 원들 각각에 대하여
            # points 각각을 반복
            # (이 방법 자체는 범용적인 건 아님)
            for pt in points:
                pt_x = pt[0]
                pt_y = pt[1]

                dist_two_sqr = (pt_x - center_x) ** 2 + (pt_y - center_y) ** 2
                dist = dist_two_sqr ** (1/2)
                # print(dist)
                # 시간을 더 줄일 수 있는(듯한) 방법
                # => 제곱하기 전에 범위 아예 벗어난 점 거르기
                if dist > center_rad:
                    continue
                else:
                    num_of_inner_points += 1
                    print(f'{one_query_crcl} / {pt}\n=> it''s okay!')

            cnt_for_each_queries.append(num_of_inner_points)

        return cnt_for_each_queries




if __name__ == '__main__':
    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]
    solve = Solution()
    print(solve.countPoints(points, queries))