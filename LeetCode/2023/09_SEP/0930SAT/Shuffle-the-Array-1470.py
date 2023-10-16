class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        dict_inc_dec = {"++X": 1, "X++": 1,
                        "X--": -1, "--X": -1}
        sum = 0
        for i in operations:
            sum += dict_inc_dec[i]
        return sum

if __name__ == '__main__':
    operations = ["++X","++X","X++"]
    solve = Solution()
    print(solve.finalValueAfterOperations(operations))