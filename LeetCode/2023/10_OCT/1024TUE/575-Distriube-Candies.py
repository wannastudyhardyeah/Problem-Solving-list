from typing import List
import collections


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        '''
            candyType에 대해서 Counter() 이용해서 set 만들기
            (Alice가 먹을 수 있는 최대 개수)가
            (candy 종류 개수)보다 많다면
            (candy 종류 개수)가 답
        '''
        # the_num_of_candy_type = len(collections.Counter(candyType))
        # howmany_candies = len(candyType)
        # alice_can_eat_at_most = howmany_candies // 2
        #
        # if the_num_of_candy_type < alice_can_eat_at_most:
        #     return the_num_of_candy_type
        # else:
        #     return alice_can_eat_at_most
        unique_candies = set(candyType)

        return min(len(unique_candies), len(candyType)//2)

if __name__ == '__main__':
    candyType = [1,1,2,2,3,3]
    solve = Solution()
    print(solve.distributeCandies(candyType))