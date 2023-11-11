from typing import List


'''참고한 곳
https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand/
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, paren_string):
            if len(paren_string) == (n * 2):
                res.append(paren_string)
                return;
            if left < n:
                dfs(left + 1, right, paren_string + '(')
            if right < left:
                dfs(left, right + 1, paren_string + ')')

        res = []
        dfs(0, 0, '')
        return res

if __name__ == '__main__':
    n = 3
    solve = Solution()
    print(solve.generateParenthesis(n))