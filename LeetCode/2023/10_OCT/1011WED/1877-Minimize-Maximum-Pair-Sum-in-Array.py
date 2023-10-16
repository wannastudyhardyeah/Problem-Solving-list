from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        print(f'sorted_nums: {sorted_nums}')
        len_nums = len(nums)
        # 큰 값 발견하면 갱신
        max_val = -1
        for i in range(len_nums//2):
            temp_val = sorted_nums[i] + sorted_nums[len_nums - 1 - i]
            if (max_val < temp_val):
                max_val = temp_val
            print(f'{i}, {len_nums - 1 - i}:\n=> {temp_val}')
        return max_val


if __name__ == '__main__':
    nums = [4,1,5,1,2,5,1,5,5,4]
    solve = Solution()
    print(solve.minPairSum(nums))