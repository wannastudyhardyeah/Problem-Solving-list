from typing import List


'''참고한 곳
https://leetcode.com/problems/generate-parentheses/solutions/1181112/easy-to-understand-python-no-recursion/
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        fixed_paren = {"()"}

        for i in range(n - 1):
            new_parens = set()
            for paren in fixed_paren:
                for j in range(len(paren)):
                    new_parens.add(paren[:j] + "()" + paren[j:])
            fixed_paren = new_parens
        return fixed_paren

if __name__ == '__main__':
    n = 3
    solve = Solution()
    print(solve.generateParenthesis(n))