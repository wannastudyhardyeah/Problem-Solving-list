from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_all = sum(nums)
        res_list = [sum_all]
        len_nums = len(nums)
        for i in range(len_nums - 1, 0, -1):
            temp_two_sum = res_list[len_nums - i - 1] - nums[i]
            res_list.append(temp_two_sum)
        res_list.reverse()
        return res_list
if __name__ == '__main__':
    nums = [1,2,3,4]
    solve = Solution()
    print(solve.runningSum(nums))