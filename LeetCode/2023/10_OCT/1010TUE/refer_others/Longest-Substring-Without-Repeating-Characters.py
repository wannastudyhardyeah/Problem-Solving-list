import re

class Solution:
    def lengthOfLongestSubstring(self, input_str: str) -> int:
        charSet = set()
        l = 0
        result = 0

        for idx_chr in range(len(input_str)):
            while (input_str[idx_chr] in charSet):
                charSet.remove(input_str[l])
                l += 1
            charSet.add(input_str[idx_chr])
            result = max(result, (idx_chr - l + 1))
        return result

if __name__ == '__main__':
    input_str = "abcabcbb"

    solve = Solution()
    print(solve.lengthOfLongestSubstring(input_str))