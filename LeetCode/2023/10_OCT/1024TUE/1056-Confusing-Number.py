import re

class Solution:
    def confusingNumber(self, n: int) -> bool:
        '''
            포함돼있으면 아예 invalid인 것
            : 2, 3, 4, 5, 7
            포함돼있어도 아예 invalid인 건 아닌 것
            : 0, 1, 6, 8, 9

        '''
        # 일단, invalid 확정적인 것부터 거르기
        str_n = str(n)
        regex_only_invalid = re.compile('[01689]*[23457]+[01689]*')
        match = regex_only_invalid.findall(str_n)
        # invalid가 된 경우임
        if (len(match) == 1):
            return False

        # 0, 1, 8 셋 중 하나로만 이뤄졌을 때
        regex_only_same = re.compile('^[018]+$')
        match_same = regex_only_same.findall(str_n)
        print(match_same)
        if (len(match_same) == 1):
            return False
        return True

if __name__ == '__main__':
    number = 20
    solve = Solution()
    print(solve.confusingNumber(number))