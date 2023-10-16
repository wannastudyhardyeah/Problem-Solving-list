class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[i]] for i in range(len(nums))]

if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    solve = Solution()
    print(solve.buildArray(nums))