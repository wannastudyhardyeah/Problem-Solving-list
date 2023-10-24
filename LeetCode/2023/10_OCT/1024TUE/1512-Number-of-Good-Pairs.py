from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
            i < j and nums[i] == nums[j]인
                    (i, j)의 개수를 구하기
        '''
        len_nums = len(nums)
        cnt = 0
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if (nums[i] == nums[j]):
                    cnt += 1
        print(cnt)
        return cnt


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    solve = Solution()
    print(solve.numIdenticalPairs(nums))