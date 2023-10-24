import re

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum_len = 0
        for letter in jewels:
            # 정규식 만들기
            match = re.findall(f"[\s{letter}]", stones)
            sum_len += len(match)
        return sum_len

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    solve = Solution()
    print(solve.numJewelsInStones(jewels, stones))