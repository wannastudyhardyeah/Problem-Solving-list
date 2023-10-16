class Solution(object):
    def getConcatenation(self, nums):
        """
        :type address: List[int]
        :rtype: List[int]
        """
        # res = [[].append(nums[i])]
        len_nums = len(nums)
        return [nums[_] for _ in range(-len_nums, len_nums)]

if __name__ == '__main__':
    nums = [1, 2, 1, 1, 2]
    solve = Solution()
    print(solve.getConcatenation(nums))