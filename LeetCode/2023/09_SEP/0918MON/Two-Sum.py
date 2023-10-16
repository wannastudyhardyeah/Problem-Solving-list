from typing import List



class Solution:
    '''
    이건 리트코드 제공 solution 中
            "Approach 2: Two-pass Hash Table"
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {num: i
                 for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if (((target-num) in table)
                and (i != table[(target-num)])):
                return [i, table[(target-num)]]
    #-------------------------------------------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         size_nums = len(nums)
#         solved = []
#         for i in range(size_nums):
#             for j in range(i+1, size_nums):
#                 temp_left = nums[i]
#                 temp_right = nums[j]
#                 if (temp_left + temp_right == target):
#                     solved.append(i)
#                     solved.append(j)
#                     return solved

import random as rd

if __name__ == '__main__':
    arr = [rd.randint(1, 15) for _ in range(10000)]
    # nums = [2, 7, 11, 15]
    nums = arr
    target = 9
    sol = Solution()
    solve = sol.twoSum(nums, target)
    print(solve)