from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, ele in enumerate(nums):
            mod_result = idx % 10
            if (mod_result == ele):
                return idx
        return -1

if __name__ == '__main__':
    nums = [4, 3, 2, 1]
    solve = Solution()
    print(solve.smallestEqual(nums))