class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        size_x = len(str_x)

        is_right = 1
        for i in range(int(size_x/2)):
            if (str_x[i] != str_x[size_x-i-1]):
                is_right = 0
                break
        if (is_right == 0):
            return False
        else:
            return True

if __name__ == '__main__':

    solve = Solution().isPalindrome(1212)
    print(solve)