# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while (i < j):
            pivot = (i + j) // 2
            # pivot 값의 버전이 bad라면
            if (isBadVersion(pivot)):
                # 현재 pivot 값을 오른쪽에 저장
                j = pivot
            else: # 아니라면
                # (pivot+1)을 왼쪽에 저장
                i = pivot + 1
        return i
if __name__ == '__main__':
    n = 5
    bad = 4
    solve = Solution()
    print(solve.firstBadVersion())